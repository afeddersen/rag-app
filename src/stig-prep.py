import subprocess

# Start the Docker container and get its ID
container_id = subprocess.check_output([
    "docker", "run", "-d", "-it",
    "--entrypoint", "/bin/sh",
    "cgr.dev/chainguard/wolfi-base:latest"
]).decode().strip()

paths = ["/etc"]

try:
    for path in paths:
        files = subprocess.check_output([
            "docker", "exec", container_id,
            "find", path, "-type", "f"
        ]).decode().splitlines()

        for file in files:
            try:
                # Read the first few bytes to check if it's likely a text file
                head_output = subprocess.check_output([
                    "docker", "exec", container_id, "head", "-c", "1000", file
                ], stderr=subprocess.STDOUT)

                # Check if the output can be decoded as utf-8, a simple heuristic for text files
                try:
                    head_output.decode('utf-8')
                    is_text = True
                except UnicodeDecodeError:
                    is_text = False

                if is_text:
                    file_content = head_output.decode('utf-8', 'ignore')  # Use head output directly
                    markdown_file_name = file.replace("/", "_")[1:] + ".md"
                    with open(markdown_file_name, "w") as markdown_file:
                        markdown_file.write(file_content)
                else:
                    print(f"Skipping binary file: {file}")

            except subprocess.CalledProcessError as e:
                print(f"Failed to process file: {file}")
                print(f"Error code: {e.returncode}")
                print(f"Error output: {e.output.decode('utf-8', 'ignore')}")

finally:
    subprocess.call(["docker", "stop", container_id])
    subprocess.call(["docker", "rm", container_id])

print("Script completed.")


