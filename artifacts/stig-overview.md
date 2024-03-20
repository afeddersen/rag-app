Executive Summary
The Security Technical Implementation Guide (STIG) is a Department of
Defense (DoD) technical guidance standard that captures the cybersecurity
requirements for a specific product, such as a cloud application going into
production to support the warfighter. System integrators (SIs), government
contractors, and independent software vendors know the STIG process as a
well-governed process that all of their technology products must pass. The
Defense Information Systems Agency (DISA) released the Container Platform
Security Requirements Guide (SRG) in December 2020 to direct how software
containers go through the STIG process.
Introduction
A STIG contains technical guidance to “lockdown” information systems that
might otherwise be vulnerable to a malicious computer attack.
While the STIG is a DoD compliance program, there are lessons that
the commercial sector can learn from STIGs because of their focus on
maintaining secure configurations. The STIG process is a study in hardening
systems and software configurations.
The tasks around STIG compliance directly apply to the healthcare, retail,
financial, and other industries that mandate secure and well-documented
systems and software to be in compliance.
We wrote Navigating Software Containers through the STIG Process to help
educate those who may be new to STIG and promote best practices to help
ensure your containers make it through the STIG accreditation process. This
guide also includes links to documentation about how you can use the new
STIG compliance check in Anchore Federal.
4
STIG 101
STIGs are the configuration standards that govern DoD information assurance (IA) and IA-enabled
devices and systems. The Defense Information Systems Agency (DISA) maintains an authoritative
library of STIGs that explain in explicit detail how to configure computing resources on DoD networks to
maximize security.
In comparison, the Security Content Automation Protocol (SCAP) synthesizes interoperable
specifications derived from community ideas.
The DoD publishes STIGs quarterly to ensure all connecting DoD organizations remain fully up-to-date
and compliant. Quarterly STIG updates provide developers with the latest information concerning:
» Hardware and software configuration
» Security protocol implementation
» Training processes
There are three STIG categories:
Category I Category I covers vulnerabilities that result in the loss of confidentiality, availability,
or integrity. Furthermore, these vulnerabilities allow unauthorized access to
classified information or facilities. Category I vulnerabilities can also lead to the
denial of service on a mission-critical system.
Suppose you don’t address category I vulnerabilities. In that case, the DoD won’t
grant you an Authority to Operate (ATO) because these risks may result in loss of
life, mission failure, or damage to facilities.
There are two exceptions for Category I risks:
» A mission-critical system
» Failure to use the system could lead to a failed mission
Category II Category II covers vulnerabilities that result in a loss of confidentiality, availability,
or integrity. Category II vulnerabilities lead to a Category I vulnerability, mission
degradation, personal injury, and damage to equipment or facilities.
Category III Category III covers vulnerabilities that degrade security measures to protect
against loss of confidentiality. Category III vulnerabilities can lead to a Category II
vulnerability, delay in outage recovery, and affect data and information accuracy.
It’s important to note that there are no generic or “one size fits all” STIG rules you can apply across
all of your applications. The “old school” approach means adjusting and tuning server policies by
application environment, server by server. Such a manual approach could potentially increase
project timelines by weeks. It also means project costs can balloon upwards of $10,000+ for a
server instance. This tedious and painstaking work often falls on system administrators, application
administrators, and information assurance staff who are pulled off their regular operations duties,
denying valuable resources to other projects.
5
Container Security Best Practices
Automate Container Scanning
Total security awareness of the software containers in your DoD project
requires automated container scanning. While automated container
scanning is already a DevSecOps best practice, STIG compliance raises the
stakes by making it a requirement. Anchore Enterprise provides a solution
that enables you to automate container scanning across your toolchains.
Create an SBOM for your Containers
A long-held STIG best practice is to document every component in your
infrastructure. A similar best practice applies to containers. You want to
create a software bill of materials (SBOM) for your containers. SBOMs play a
major role in the Executive Order on Improving the Nation’s Cybersecurity.1
Read Getting to Know and Love Your Software Bill of Materials on the
Anchore Blog to learn more about the SBOM.
A well-defined SBOM gives your DevOps and security teams the most
accurate documentation of what each software container in your project
includes. The SBOM documents all the elements. This valuable insight
enables teams to ensure that they are not including any malicious or
vulnerable software that could be harmful to their organization or the
organizations of their customers and clients.
STIG Tips and Best Practices
STIGs are notorious for their complexity and the hurdle that STIG compliance
poses for technology project success in the DoD. Here are some tips to help
your team prepare for your first STIG or to fine-tune your existing internal
STIG processes.
Foster STIG Expertise Internally
There’s a lot of out-of-date and conflicting information about the STIG
process on the web today. System integrators and government contractors
need to build STIG expertise across their DoD project teams to cut through
such noise.
Including STIG expertise as an essential part of your cybersecurity team is
the first step. While contract requirements dictate this proficiency, it only
helps if your organization can build a “bench” of STIG experts.
1. https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/
6
Here are three tips for building up your STIG talent base:
» Make STIG experience a “plus” or “bonus” in your cybersecurity job requirements
for roles, even if they may not be directly billable to projects with STIG work (at
least in the beginning)
» Develop internal training around STIG practices led by your internal experts
and make it part of employee onboarding and DoD project kickoffs
» Create a “reach back” channel from your project teams needing STIG expertise
to other parts of your company such as corporate and other project teams
with STIG expertise to get their support for any issues and challenges with the
STIG process
Depending on the size of your company, clearance requirements of the project, and
other situational factors, the temptation might be to bring in outside contractors to
shore up your STIG expertise internally. For example, the Container Platform Security
Resource Guide (SRG) is still new, and it makes sense to bring in an outside contractor
with some experience managing containers through the STIG process. If you go this
route, be conscious of knowledge transfer from the contractor to your internal team.
Otherwise, their container and STIG knowledge walk out the door at the end of the
contract term.
Validate your STIG Source Materials
When researching the latest STIG requirements, you need to validate the source
materials. There are many vendors and educational sites that publish STIG content.
Some of that content is outdated and incomplete. It’s always best to go straight to
the source. DISA provides authoritative and up-to-date STIG content at https://public.
cyber.mil/stigs/downloads/.
Make the STIG Viewer part of your Approved Desktop
Working on DoD and other public sector projects requires secure environments for
developers, solution architects, cybersecurity specialists, and other team members.
The STIG Viewer available from https://public.cyber.mil/stigs/srg-stig-tools/ should
become a part of your DoD project team’s secure desktop environment. Save the extra
step of your DoD security teams having to put in a service desk ticket to request the
STIG Viewer installation.
Include a Technical Writer on your Cybersecurity Team
The STIG process is writing and reviewing intensive. Look for ways to include a technical
writer with your cybersecurity team to work with them during the STIG development
process. While a technical writer doesn’t have to be a STIG specialist, a writer with
experience documenting systems and infrastructure can serve as a needed level of
quality assurance for your team that’s working through the STIG process.
7
Containers and the STIG Process
Docker Enterprise was the first container platform to pass the STIG process.2 For forward
looking programs, Platform One and now Space Force have put containers at the forefront of
their DevSecOps and security strategies. The STIG process is developing to meet the needs and
challenges of cloud-native software development.
As per a November 20, 2020 memo, the Defense Information Systems Agency (DISA)
in accordance with DoD Instruction 8500.01, released the Container Platform Security
Requirements Guide (SRG) Version 1, Release 1 for immediate use. The document is available for
download from https://cyber.mil/ (CAC Card access required) and https://public.cyber.mil.
The Container Platform SRG provides technical requirements for securing a container platform.
This SRG defines containers as:
“high-level software with the capability of managing container lifecycles.
A container platform includes a container engine or runtime, container
registry, and key-value store (i.e., components). With the platform, services
such as a DNS, firewall, router, and web console may also be deployed.”
The container platform is the software used to orchestrate the execution of the container.
Here are some examples of commercial and OSS containers found in the DoD:
2. https://www.docker.com/blog/docker-enterprise-first-disa-stig-container-platform/
3. Docker EE is the container platform although it looks like this became Mirantis Kubernetes
Engine post-acquisition: https://www.mirantis.com/software/mirantis-kubernetes-engine/
Container Orchestrator Description
Kubernetes Core technology - upstream
Open Shift Container platform
Konvoy Container platform
Tanzu Container platform
Docker Container engine3
Rancher Container platform
8
This platform may have other services to aid in the overall orchestration such as routing,
DNS, and firewalls. Each container platform has an individual STIG. You can review these
to learn more about their specific security settings. Container Platform SRGs are also a
valuable resource for best practices and include all applicable baseline technical NIST SP
800-53 requirements.
CNSSI 1253 defines the required controls for DoD systems based on confidentiality, integrity,
and availability (baseline) of the information system.
When you run a STIG compliance check using Anchore Federal, the check happens in the
container. When an image is instantiated into a container, the image itself is not changed;
instead, a copy of it is placed within the container platform and becomes a running
instance of the application.
The container platform runtime should be configured to pull the most up-to-date version
of an image from the registry so that applications are always current. Continuous delivery
automation enables developers to build a new version of the image for their application,
test the image, push it to the container platform registry, and then rely on the automation
tools to deploy it to their target environments. A developer is generally responsible for
patching and configuring a new image when building a new image version.
It is essential that data be protected when it is transmitted, whether it is between the
user and the service, between components, or during data image pulls. An adversary
would be able to compromise all data on a container platform if they were successful in
compromising the data.
Benefits
Here are some benefits of using containers to meet STIG compliance standards:
» Containers are foundational to DevSecOps in the commercial and public sectors
» Vulnerability scanning of containers can take place at all stages of a DevSecOps
pipeline with the caveat that the container must be present as an image or
instantiated as a running container.
» DoD programs can reuse container images by storing them in a centralized and
secure repository, provided the container image artifact has passed the STIG
evaluation process.
Challenges
Here are some challenges that containers pose in the STIG compliance process:
» Container development and security expertise are still very much in short supply in
the DoD and the system integrator community
» Containers are not yet a common development standard across DoD projects
» DoD sponsored container STIG training isn’t readily available
9
Kubernetes and the STIG Process
In December 2020, DISA released a draft STIG for Kubernetes for comment by the industry.4
The STIG went final on April 21, 2021.5 This STIG covers the following:
Hosting Operating Systems
The Kubernetes STIG addresses operating system file permissions for Kubernetes files, but
within an operating system, there are settings and processes outside the realm of the
Kubernetes STIG. According to this STIG, there may also be instances where a Kubernetes
requirement can be met, but without the operating system requirement being met, the
cluster isn’t fully secure.
Securing the Kubernetes cluster requires defining user roles correctly. It is often the case
that all users of an operating system have the same role. Giving users more privileges than
necessary allows a user to escalate their privileges and make Kubernetes cluster changes,
an administrator function. It is crucial to look at the roles your agency wants to implement
for privileged users and give users only the roles required for carrying out their duties.
The permissions laid forth by the operating system requirements may or may not be stricter
than those of the Kubernetes STIG requirements for privileges and ownership according to
the STIG. Care must be taken to give the least privileges and ownership to Kubernetes files
and still allow operation of Kubernetes and the hosted services.
Kubernetes Management
The STIG specifies that no matter the method used for Kubernetes cluster management,
users must be authenticated using common access card (CAC) credentials. The validation
of CAC credentials will not be done by Kubernetes but by the operating system or local and
remote access host system access controls.
Kubernetes Component Authentication
In addition to having a secure connection, the relationship between Kubernetes components
must be trusted according to the Kubernetes STIG. For a component to identify itself,
certificates are used. These certificates must be protected and tied to a trusted certificate
authority (CA). By using only certificates from a trusted CA, the use of self-signed certificates
is not permitted. In a DoD environment, the DoD should be the CA and issue certificates.
Transmitted Data Protection
Transmitted data must be protected, whether between the user and a service within
Kubernetes, intercomponent communication, or data image pulls according to the
Kubernetes STIG. If an adversary were able to compromise the data, the entire Kubernetes
cluster would be compromised.
4. https://public.cyber.mil/announcement/request-for-comments-disa-has-released-the-draft-kubernetes-stig-for-review/
5. https://public.cyber.mil/announcement/stig-update-disa-has-released-the-kubernetes-security-technical-implementation-guide-stig/
10
Inside the STIG Process for Containers
Notable highlights from the SRG:
General Security Requirements
DISA is quick to point out that container platform security
goes well beyond just the configuration settings. They layout
the following considerations for container security:
» Services being hosted
» User community
» Data being accessed
» Where the container will reside
Not looking beyond the container platform opens you up
to security compromises and implementation issues that
could result in breaches of classified information.
Hosting Operating Systems
The Container Platform SRG addresses operating system
file permissions for container platform files. Still, within an
operating system, some settings and processes are outside
the realm of the Container Platform SRG.
The SRG also addresses instances where a project team
can meet the container platform requirement. However,
the team may not meet the operating system requirement.
Consequently, the container platform is not fully secure.
To secure the operating system properly, you should use the
appropriate Operating System SRG or specific vendor STIG.
Roles
The SRG also stresses the importance of defining user roles
properly to secure a container platform.
Container Platform Management
As more DoD projects move to Kubernetes and other
orchestration platforms, the SRG sets up best practices
Questions to ask from
the Container Platform
Security SRG
The Container Platform SRG Technology
Overview includes the following questions
about containers:
• Are the user container images following
application guides and container best
practices?
• Are all of the components and services
hardened according to guidance
within the technology SRG or more
specific technology STIG?
• Are all components and services
following ports and protocol guidelines
set forth by DoD Instruction 8551.01
policy?
• Are all endpoints trusted and
communication channels encrypted?
• Are workloads, user groups, and
data sensitivity levels being isolated
properly?
• Is there a process for introducing new
container images into the production
environment?
• Are the security tools monitoring
the components and user services
container aware and designed to
operate at the scale and change rate
typically seen with containers?
• Are the containers being run with
policies to limit resource usage such as
CPU, storage, and memory? 
11
Vendor STIGs
If your company is or wants to sell products to DoD customers, you can be proactive
and write STIGs for your products by following a process from the DISA Risk Management
Executive (RME). Unlike FedRAMP, It’s not necessary to have a federal agency sponsor before
you embark on creating a STIG for your products.
Here’s the high-level process you’ll follow:
» Complete the Vendor STIG Intent Form available under Guidance Documents on
cyber.dod.mil.
» Submit your completed form to disa.stig_spt@mail.mil.
» A RME STIG team representative contacts you to start the STIG process.
» Complete the SRG spreadsheet
Upon completion of the SRG spreadsheet, the data is transformed into a STIG. The STIG,
once written, will reflect what a specific product CAN do, in a specific release and possible
patch level. Published STIGs only contain requirements that fall into the “applicable and
configurable” category.
Technology-specific SRGs reflect what a technology family SHOULD be capable of, to be
secured. The STIG author (vendor) will assess the SRG controls against a product with one
of four potential outcomes.
Outcome Description
Not Applicable The feature does not exist in the product,
and therefore cannot be exploited
Applicable – configurable This feature may or may not meet the
requirement based on settings
Applicable – inherently meets This feature isn’t configurable but meets
the requirement by default
Applicable – does not meet – not
configurable
This feature doesn’t meet the
requirement
