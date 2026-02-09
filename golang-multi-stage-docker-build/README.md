# Single-stage Build
A single-stage build uses a single FROM instruction in the Dockerfile. All required tools, dependencies, source code, and build artifacts remain in the final image.

# Multi-stage Build
A multi-stage build uses multiple FROM instructions in the Dockerfile. Each FROM instruction begins a new stage. Assets from previous stages can be selectively copied to the final stage, allowing unnecessary build tools and dependencies to be excluded from the final image.

<img width="900" height="265" alt="image" src="https://github.com/user-attachments/assets/3e98536f-7d90-4f9c-98f6-e72b66d3fc7f" />
