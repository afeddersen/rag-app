1. OVERVIEW
1.1 Introduction
This document focuses on the Department of Defense (DOD) Enterprise DevSecOps Initiative
(DSOP) and was created to detail the Enterprise DevSecOps Container Hardening Process and
ensure it meets the DOD Hardened Containers Cybersecurity Requirements. It is important to
understand both DevSecOps and cybersecurity concepts and principals, as well as have
knowledge of containers and container platforms. Refer to the Master Approach Document for
more information on how the DSOP platform functions.
DevSecOps is a set of software development practices that combines software development
(Dev), security (Sec), and information technology operations (Ops) to secure the outcome and
shorten the development life cycle. Software features, patches, and fixes occur more frequently
and in an automated fashion. Security is applied at all phases of the software life cycle. An
example DevSecOps process is shown in Figure 1-1 below. This document will focus on the
process of securing containers that are placed into a common repository for everyone to use. This
repository can be found at https://repo1.dsop.io/dsop (refer to Figure 1-2).
Note: This document focuses on container security. It is understood that any application code or
library must be scanned by static/dynamic code analysis tools and passed or have
mitigated/accepted the risk prior to being integrated into a container for DOD use. If the
application is already approved for use (and scanned) by the Intelligence Community
(IC)/National Security Agency (NSA)/DOD Chief Information Officer (CIO)/Defense
Information Systems Agency (DISA), reciprocity can take effect. This document does not
describe that process.
Figure 1-1: DevSecOps Example
UNCLASSIFIED
Container Hardening Process Guide, V1R2 DISA
24 August 2022 Developed by DISA for the DOD
2
UNCLASSIFIED
Figure 1-2: Iron Bank Repository
1.2 Definitions
In describing the hardening process, it is necessary to define concepts and terminology. This
section will define and describe items discussed in the process as well as other sections of this
document.
1.2.1 DOD Hardened Containers (DHC)
A DOD hardened container is an Open Container Image (OCI)-compliant image that is secured
and made compliant with the DOD Hardened Containers Cybersecurity Requirements.
Container images should adhere to the OCI Image Format Specification to ensure portability
whenever possible. These containers are made available for use in the Iron Bank, the centralized
repository.
1.2.2 Container Hardening Team (DHT)
The Container Hardening Team is responsible for hardening DOD containers according to DOD
Hardened Containers Cybersecurity Requirements. The team is composed of DevSecOps
Engineers and other container experts that have knowledge of the product being hardened.
They also have an understanding of the DHC Cybersecurity Requirements and DISA Security
Requirements Guide (SRG) and Security Technical Implementation Guide (STIG) information.
A single team member is called a Hardener.
Hardeners also require the following skills:
• Expertise in OCI-compliant container images, including creating compliant Dockerfiles.
• Understanding of DISA STIG/SRG documentation as it applies to the application run.
UNCLASSIFIED
Container Hardening Process Guide, V1R2 DISA
24 August 2022 Developed by DISA for the DOD
3
UNCLASSIFIED
• Expertise in the DHC Cybersecurity Requirements.
• Strong understanding of Container security solutions (Prisma, Anchore, and StackRox)
for vulnerability scanning, Chef InSpec and OpenSCAP for compliance scanning.
1.2.3 DOD Container Factory (DCF)
To automate the hardening process, the DOD has implemented a DSOP platform on GovCloud
at Impact Level 2 (publicly accessible and open-source) to set up the Continuous Integration/
Continuous Delivery (CI/CD) pipeline leveraged to automate the container hardening process.
This DevSecOps process is similar to Figure 1-1 and will be used primarily for the validation of
hardened containers.
1.2.4 Repo One/DOD Centralized Container Source Code Repository (DCCSCR)
This is the web location used to store the hardened Dockerfiles and associated documentation.
This DOD enterprise source code repository will be centrally hosted so Hardeners can store their
code and leverage a CI/CD pipeline.
For onboarding containers into Repo One, view the prerequisite information shown at
https://repo1.dsop.io/dsop/dccscr/tree/master/contributor-onboarding or view the process detail
in Section 2.
1.2.5 Iron Bank/DOD Centralized Artifacts Repository (DCAR)
This is the system that stores the DOD Hardened Containers and associated documentation. This
DOD enterprise centralized artifacts repository is implemented on a DOD Approved Cloud to
provide access to DOD Programs and to the DOD Hardened Containers.
The artifact repository supports both files (traditional artifacts) and containers, as well as
container registry capabilities. It provides a secure mechanism to store, track, sign, and distribute
approved containers. It is accessible at: https://ironbank.dsop.io.
1.2.6 DOD Approved CI/CD Orchestration Solution (DACCOS)
In a DevSecOps system, a CI/CD pipeline is integral, and an orchestration solution is needed.
The DoD has chosen CI/CD orchestration solutions such as Jenkins (open source), Cloudbees
Jenkins, and GitLab for this function, and all are containerized and hardened where applicable.
1.2.7 DOD Base Container Image Approved Source (DBCIAS)
To ensure container base images are from approved sources, a container base image must be
downloaded from a DBCIAS as a baseline.
There are two types of repositories: trusted and untrusted. Trusted repositories are used as an
approved source for downloading container base images. Untrusted resources cannot be used in 
UNCLASSIFIED
Container Hardening Process Guide, V1R2 DISA
24 August 2022 Developed by DISA for the DOD
4
UNCLASSIFIED
this fashion unless a Memorandum of Understanding (MOU) is reached between the DoD and
the vendor or mission partner using the untrusted source. The MOU will dictate strict levels of
security and ensure access to base images and their updates.
The following sources are currently approved and should be used in order of priority:
• Iron Bank/DCAR (approved DOD-wide; trusted).
• Product vendor proprietary repository (untrusted).
• Docker Hub (untrusted).
• Red Hat Container Repository (untrusted).
A trusted repository indicates that the containers were hardened by the DHT and can be used as
is. Refer to Section 2.1 for the vendor/mission partner prerequisite review steps before selecting
a base image.
UNCLASSIFIED
Container Hardening Process Guide, V1R2 DISA
24 August 2022 Developed by DISA for the DOD
5
UNCLASSIFIED
2. CONTAINER HARDENING PROCESS
The container hardening process requires the mission partner work closely with the DOD
Container Approvers and Hardeners so that cybersecurity confidence can be gained about the
containers prior to DOD use.
2.1 Container Hardening Prerequisite Steps
Some key prerequisite steps are listed below. The DHT is available to assist all personnel if there
are questions.
1. Always prioritize the reuse of a Dockerfile from
Iron Bank. Alternatively, a Dockerfile from its
vendor or open-source community can be reused if
it can be switched to an approved DOD base
image. Ideally, the team should ensure the Iron
Bank’s accepted base images
(UBI7/UBI8/scratch/distroless) are used by
upstream partners/vendors.
2. Ensure the Dockerfile uses a DOD- hardened/
approved base container whenever available. Use
the FROM command to do this. For example, if the Jenkins Dockerfile uses the Docker
Hub OpenJDK base image, ensure the FROM instruction is replaced by the DoDhardened OpenJDK base image instead. Use of the STIGed DOD-approved Universal
Base Image (UBI) is recommended, as is the use of the approved DOD scratch and
distroless image. These are open source, free, and available on the Iron Bank.
3. Use base images that reuse the closest hardened image layer available to inherit its
hardening. For example, if a Java application is used, use the base image of the DODhardened OpenJDK and not just the DOD-hardened UBI image. It is highly
recommended to have the DOD Enterprise DevSecOps team review and agree to the
selection of a base image if it does not come from the Iron Bank.
4. If there are multiple source options/tags/variants for the base image chosen, ensure the
image is scanned with both Prisma (or StackRox) and Anchore, to understand security
risks associated with each image. For example, if you can download the image from
Docker Hub, RedHat registry or Oracle registry, select the image most closely aligned
with the DOD Hardened Containers Cybersecurity Requirements based on the scan
results of those images.
5. If the base image has security flaws such as critical vulnerabilities, attempt to mitigate the
flaw by applying security hardening, configuration changes etc. If that does not correct
the flaw, the library/binary impacted must be removed or the risk documented as
accepted.
6. Prepare all dependencies in the Repo One prior to submitting for hardening. All
dependencies that need to be downloaded from the internet must be included in the
Download.json or Download.YAML file to allow the container hardening system to build
containers offline. If a container can benefit the DOD, then it can be considered for
inclusion in Repo One or another repository compliant with the DOD Enterprise
Tech Note: A Dockerfile execution must
begin with a FROM instruction. This may
be after parser directives, comments, and
globally scoped ARGs. As an argument, a
name is provided with an optional tag for
an image that should be used as the base
for the Docker container. Instead of
building a host OS from scratch, the
FROM instruction allows a base image
for Linux or another OS as the Dockerfile
basis.
UNCLASSIFIED
Container Hardening Process Guide, V1R2 DISA
24 August 2022 Developed by DISA for the DOD
6
UNCLASSIFIED
DevSecOps Reference Design. The platform and hardened containers must be compliant
with the minimum viable product requirements or it cannot be accredited.
7. It is critical for containers to be able to be built on
classified and air gapped environments. Dockerfiles
should not download any artifacts. Instead, a
prephase step called Download will occur so the
platform can download the required dependencies
online. Then, the rest DOD Container Hardening
process will operate in a disconnected and/or
classified environment that does not have internet
access. This will ensure the process will not be able
to pull files from the internet that are required to
build.
8. If an organization that has a capability, has two license options (for example, open source
and an enterprise managed version), both containers must be provided to Repo One. The
organization cannot only provide the paid version. The DOD Hardening Team will not
accept enterprise containers if the open-source container is not also provided.
2.2 Container Hardening Process
The process described in this section is for vendor or mission partner informational awareness. It
is important for mission partners and vendors to understand the best practice considerations
shown in Appendix D: Container Security/Remediation Considerations. It is also important to
understand that as containers inherit many of the security controls from the underlying Platform
as a Service (PaaS) solution, the underlying host OS must be hardened per Agency-specific
security guidelines as listed in Appendix C: Security Control Inheritance.
It is important to understand that containers must run on a DevSecOps Platform compliant with
the DoD Enterprise DevSecOps Ref Design and its MVP requirements, including the Sidecar
Container Security Stack, which enforces behavior detection and zero trust in runtime.
Without a CNCF-compliant Kubernetes platform and the MVP Ref Design capabilities, a
standalone container is not accredited and its certificate to field does not apply.
The container hardening and scanning pipeline is located at https://repo1.dsop.io/dsop. Note that
third parties are not allowed master branch write access to the Repo One repository; only
members of the Hardening Team are authorized to make changes that will affect hardened
containers including, Dockerfiles, readme files, license files, and anything else required for the
scanning and hardening of the container. A Container Hardener will approve the container into
the Repo One and Iron Bank repository after validation and approval. This process should also
support free and open-source software (FOSS) as well as commercial off-the-shelf (COTS)
software.
Using the container software factory or pipeline, the Hardener will begin the hardening process
as depicted in the Figure 7-1 sub-process titled “Begin Hardener process”. The detailed steps and
examples are shown in Table 2-1 below.
Tech Note: Platform One spends a great
deal of time to ensure dependencies are
not downloaded without their knowledge.
Initially, Platform One will list all
dependencies, download them while
connected to internet, go Offline, and
build the container validating the
dependency downloads are not attempted.
This critical security process ensures
decoupling the download from the build
process.
UNCLASSIFIED
Container Hardening Process Guide, V1R2 DISA
24 August 2022 Developed by DISA for the DOD
7
UNCLASSIFIED
Table 2-1: Hardener Process
Step Process Description Example Resource
1 Create a new folder in Repo One under
the organization name.
Refer to Appendix A: Folder Structure
Example. If open source, list as open
source.
Hardener
2 Set up a new folder in the Repo One
under the product name.
Note: If a product has multiple variant
options such as “cli” mode or
“daemon” mode or x86 versus x64
versions, various subfolders can be
created for each variant.
Refer to Appendix A: Folder Structure
Example.
Hardener
3 Define and list which version of the
product and hardened containers will
initially be supported.
If a Hardener needs to harden
“Jenkins” with UBI base image, and
the current OSs supported on Docker
Hub are 2.59 to 2.60, the Hardener
should start with 2.59 and move to the
latest version, ideally using the same
documentation with attempted reuse of
the same Dockerfile created across
versions.
Note: Hardening a different OS
requires the OS to be STIGed! Use
STIGed UBI OSs if possible.
Hardener
4 Select a DoD Base Container Image
Approved Source to download the
base image from for each version.
Iron Bank is the DoD trusted
repository, for example.
Hardener
5 Set up a subfolder within Repo One
for each new version that will contain
the newly created Dockerfile and
related
scripts/documentation/LICENSE/REA
DME
.md.
Under “Open-source” and under
“Jenkins” a subfolder (“2.59”, “2.60”,
etc.) will be created per version. Refer
to Appendix A: Folder Structure
Example.
Hardener
6 Within each version, starting with the
lowest version supported, create a
Dockerfile in Repo One that will use
the selected base image. The
Dockerfile will download the
appropriate base image.
The Dockerfile will also have
additional instructions used to harden
To understand which instructions are
required, the Hardener will make
decisions based on the Scanner
findings from the scan process. Refer
to Section 2.3.
Hardener
UNCLASSIFIED
Container Hardening Process Guide, V1R2 DISA
24 August 2022 Developed by DISA for the DOD
8
UNCLASSIFIED
Step Process Description Example Resource
the container based on the Hardener
decisions to mitigate findings and/or
ensure proper DoD compliance.
Note: It is imperative to reuse instructions as much as possible between versions so hardening
can be leveraged across versions. It is understood that new versions bring additional or new
features, which can require additional hardening. Therefore, the Dockerfile should be reused
from version minus one (if it exists) to avoid redundant work and leverage prior work.
2.3 Container Scanning Process
Using the CI/CD orchestration tool, the Repo One folder content will be downloaded into the
pipeline and the Dockerfile used to build the container using Docker. This is done by reusing the
Jenkins file.
Table 2-2: Scanning Process Steps
Step Process Description Example Resource
1 The CI/CD pipeline will be triggered
once the files are placed in the Repo
One folder. Health and readiness will
then be assessed.
Hardener
2 The pipeline will automatically begin
to run the necessary scanners
connected to it for compliance and
vulnerability checks. It is mandatory to
execute both Anchore and
Prisma/StackRox checks. For Atomic
OpenSCAP or Docker OSCAP, one
must be run.
System
2a Repo One Prisma/StackRox– BSH
compliance rules will be loaded into
the product for policy checks. Using
the containers hardened from Repo
One is mandated to ensure the proper
policies are loaded and updated. This
step is mandated.
Prisma/StackRox configuration must
set SCAP_ENABLED to true.
Scanner must have updated
vulnerability information prior to
every run.
Hardener
2b Repo One Anchore – JSON xml
compliance rules must be loaded into
the product for policy checks. Using
the containers hardened from Repo
One is mandated to ensure the proper
policies are loaded and updated. This
Custom policy checks can be made.
Scanner must have updated
vulnerability information prior to
every run.
Hardener
UNCLASSIFIED
Container Hardening Process Guide, V1R2 DISA
24 August 2022 Developed by DISA for the DOD
9
UNCLASSIFIED
Step Process Description Example Resource
step is mandated along with
Prisma/StackRox.
2c Atomic OpenSCAP – This product
will operate on the command line to
provide additional CVE and
compliance scans. If Atomic
OpenSCAP is not used, Docker
OSCAP must be used.
The focus is to manage Atomic host
system and containers. For additional
information, refer to “Atomic vs.
Docker- OSCAP Whitepaper” by
DISA.
Hardener
2d Docker-OSCAP – OpenSCAP
provides vulnerability and compliance
scanning for Docker images and
containers. If Docker OSCAP is not
used, Atomic OpenSCAP must be
used.
The focus is on Docker images and
containers. For additional information,
refer to “Atomic vs. Docker-OSCAP
Whitepaper” by DISA.
Hardener
3 If findings exist, continue to the
mitigation process in Section 2.4;
otherwise, continue to the approval
process in Section 2.5.
Hardener
2.4 Findings Mitigation Reporting
Once findings are produced, it is necessary to report on these findings to the DevSecOps
Approver as well as the mission partner or vendor. Table 2-3 lists some of the common
recommendations made to mission partners and vendors.
Table 2-3: Mitigation Recommendations
Step Process Description Vendor/Partner
Recommended Action Resource
1 Iterate through the results, creating
mitigation Dockerfile instructions for
the mission partner or vendor.
1a Check base images, ports and list
findings.
Enable or disable all ports except for
those that are necessary to operate.
Change operating ports to numbers
other than standard 443 or 80.
Hardener
1b List lack of transmission security if it
exists.
Ensure that data in transmission is
secured using TLS. Strive for TLS
v1.3.
Hardener
1c List default configurations in use. Disable unused features and modify
default configurations to reduce the
possible security breach footprint.
Hardener
UNCLASSIFIED
Container Hardening Process Guide, V1R2 DISA
24 August 2022 Developed by DISA for the DOD
10
UNCLASSIFIED
Step Process Description Vendor/Partner
Recommended Action Resource
1d Emit logs to stdout. Logs must be emitted to stdout or
accessible locations.
Hardener
1e User privileges Do not run with elevated privileges.
Root ID (UID 0) must not be used
unless risk accepted and documented.
Hardener
1f Decouple configurations to make them
more portable. Use secrets for
sensitive information such as tokens,
keys, and passwords.
Use arguments, environment variables
and configmaps for configurations and
key value pairs. Also, use encoding
such as base64 to obfuscate and
encrypt yaml secrets.
Hardener
1g User access Integrate with the DoD hardened
Keycloak SSO stack for single sign on
capability or Require Common Access
Card (CAC) access through SAML
when possible. If not possible, MFA
may be used based on risk acceptance.
Hardener
1h Ensure secure connections are
leveraged.
Use TLS and secure certificates when
connecting with other services and
containers. Refer to 1b.
Hardener
1i Remove unnecessary packages,
services, and applications.
Remove anything not core to the
operation of the container.
Hardener
1j Remove User and Group permissions. Remove the setuid and setgid
permissions so that file permissions
cannot be modified for malicious
purposes.
Hardener
1k Comply with DoD Hardened
Containers Cybersecurity
Requirements.
Refer to Appendix B: DoD hardened
Containers Cybersecurity
Requirements.
Hardener
1l Avoid command injections. Be cautious with command injections
in RUN, particularly when using ENV
or ARGs.
Hardener
1m Leverage Kubernetes secrets Ensure that Kubernetes Secrets and/or
secrets vault are used to store secrets.
Hardener
2 Perform a container HEALTHCHECK
to ensure proper overall functionality
as well as the health and readiness of
the container.
Hardener
UNCLASSIFIED
Container Hardening Process Guide, V1R2 DISA
24 August 2022 Developed by DISA for the DOD
11
UNCLASSIFIED
2.5 Approving Process
From the mitigation reports, the DevSecOps Approver can determine if the results warrant
approving the container. The four options are as follows: Rejected, Conditional Approval with
Time Limit, Conditional Approval, and Approved. Each option is explained in more detail
below.
• Rejected – The container has been reviewed and it was determined that it does not meet
DoD standards for DOD enterprise-wide distribution.
• Conditional Approval Time Limit – The container will be approved provided the
findings are remediated or mitigated within a configurable number of days, dependent
upon the organization directive.
• Conditional Approval – The container has been approved with current mitigations in
place.
• Approved – The container has been approved for distribution as is.
The Approver will reach a decision on each container via a process that depicts the number and
severity of findings from the reporting performed in Section 2.4. For example, if the number of
findings is high but most are high to low, the approver may reject the container altogether due to
the magnitude of findings. If the Approver determines a critical finding exists that is key to
keeping the DOD secure, the container may be rejected. Conversely, if the finding report dictates
that the container only has a few low to medium findings, the container may be approved in its
entirety.
The level of acceptable risk for cybersecurity findings that cannot be remediated at the time of
processing will be decided on a case-by-case basis. These will all be reviewed by the Iron Bank
or the PMO Authorizing Official (AO).
Regardless of the outcomes from the Approval process, all findings and recommendations are
shared with the mission partner or vendor. If a container is placed in the Approval Time Limit
process, the container is placed into a file with a trigger for rerun at X time and date. For any
containers approved, the following steps will be performed.
Table 2-4: Approved Container Deployment Process
Step Process Description Example Resource
1 The container is signed and checksum
is created.
Container is signed with a DOD
approved key and a checksum created
using SHA 256 or more.
Hardener
2 Copy Helm/Operators and the
README/LICENSE file
Hardener
3 Checksum and artifact storage Store checksum and public key
alongside artifact in Iron Bank.
Hardener
4 Store Repo One files in DCAR as
preproduction.
Store files and tag version as
preproduction until CtF, at which time
it will be tagged as production.
Hardener
UNCLASSIFIED
Container Hardening Process Guide, V1R2 DISA
24 August 2022 Developed by DISA for the DOD
12
UNCLASSIFIED
Step Process Description Example Resource
5 Scripts used for automation Scripts used to automate deployment
or facilitate adoption must be stored
under a “scripts” folder.
Hardener
6 Configuration files for containers Configuration files for specific
container configurations must be
stored under a “config” folder.
Hardener
7 Helm charts and Kubernetes Operators Helm charts or Kubernetes operators
should be stored in Iron Bank and
Repo One to facilitate adoption.
Hardener
8 Additional documentation along with
base container documentation
Documentation necessary to
accompany container must be copied
into both repositories under a
“documentation” folder.
Hardener
9 README files Vendor or Hardener should provide a
README.md file within the subfolder
that includes the impact level for
which the container is intended.
Hardener
10 Scan results Results from Scan tools will be copied
into compliance folders as HTML files
and placed into Iron Bank repository.
As Prisma/StackRox and Anchore are
widely available and can be run by
anyone, the scan results are NOT
considered FOUO.
Hardener
11 Risk Management Risk Management documentation
created by the Hardener to document
findings, false positives, accepted
risks, and current container risk
posture will be stored in a subfolder
called “accreditation” in both
repositories.
Hardener
12 Changelog Changelog will be added to both
repositories’ subfolders and updates as
appropriate.
Hardener
13 Examples Examples can be added to support
container adoption. These will be
stored in an examples folder in both
repositories.
Hardener
14 Licensing Each hardened container requires a file
that describes the licensing required to
run the container (LICENSE). This
Hardener
UNCLASSIFIED
Container Hardening Process Guide, V1R2 DISA
24 August 2022 Developed by DISA for the DOD
13
UNCLASSIFIED
Step Process Description Example Resource
information (including files) should be
duplicated in both repositories.
README.md will also indicate if a
product requires a commercial license.
Note: Ensure any changes to the Repo One folder are changed in Iron Bank as well. If a
Dockerfile changes, the new artifact must go through the hardening process again.
2.6 Automated Hardening
The hardening process should be fully automated. When a new release is detected by the
pipeline, files are automatically downloaded from the repository and the steps are automatically
run as listed in the prior process tables. The pipeline will be configured to search for updated
dependencies/binaries and automatically run these with the pipeline, as well as notify the team of
the build results. It is important for vendors and mission partners to note that files
(artifacts/binaries) will be pulled from their existing agreed sources; it is not acceptable to host
binary files on Repo One.
If a new CVE is detected in an upgrade, the build will stop and a manual assessment of the new
CVE will be conducted.
2.7 Third-Party Container Sharing
Third parties must provide complete Dockerfiles, download.json/yaml file, scripts, and config
files so new folder creation and ingestion into Repo One can take place. Binary container images
will not be accepted and Dockerfiles must be provided to replicate the build.
It is allowed to leverage binaries (as long as they are downloaded by the Download.json or
Download.yaml script) in Dockerfile for the application layer but the source of the Dockerfile
must be provided so the container can be rebuilt. The goal is to integrate existing Dockerfiles
into the DOD hardening process and Repo One so that new containers benefit from the same
automation.
2.8 Keycloak Integration
Keycloak provides a centralized, delegated administrative model and single sign-on (SSO)
capabilities to an organization. Keycloak leverages DOD Public Key Infrastructure (PKI) and
stores information about objects on the network and makes this information available for
administrators and users to find and utilize. Keycloak uses a structured data store as the basis for
a logical, hierarchical organization of directory information. For DOD access, organizations need
the ability to use the CAC as the principal card to enable physical access to buildings and
controlled spaces as well as access to the DOD computer network and systems.
As Keycloak is fully integrated with the DOD Active Directory Federation Services
(ADFS)/PKI, it is strongly recommended that any system operating in Impact Level 4 or higher 
UNCLASSIFIED
Container Hardening Process Guide, V1R2 DISA
24 August 2022 Developed by DISA for the DOD
14
UNCLASSIFIED
use Keycloak for any user authentication. For nonperson entity-to-entity communication, signed
x509 certificates and PKI should be used.