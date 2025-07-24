# github-stats-api-cli
A Python-powered command-line interface that retrieves and displays real-time GitHub user statistics using the GitHub REST API. Designed for engineers who want fast access to clean, structured GitHub data right from the terminal.

Features
Fetches GitHub username, bio, location

Displays public repository count, followers, and following

Built with modular Python scripts for easy extension

CLI-ready for integration into automation or pipelines

Directory Structure
github-stats-api-cli/
├── github_stats/ → Python package
│ ├── init.py
│ ├── fetcher.py → Handles API calls
│ └── formatter.py → Formats response output
├── main.py → CLI runner
├── requirements.txt → Python dependencies
├── README.md → Project documentation

Setup Instructions
Clone the repository or download the folder

Navigate into the project directory:

Example: open the folder named github-stats-api-cli

Install required packages listed in requirements.txt using pip

Ensure Python is installed on your machine

Usage
To use the CLI tool, run the file main.py and provide a valid GitHub username as input.
It will fetch and display the stats directly in your terminal or output window.

Example username: vinnybeast

Sample Output
GitHub Stats for: vinnybeast
Bio: Software Engineer | Data Engineer | 
Public Repositories: 12
Followers: 83
Following: 25
Location: Nairobi, Kenya

Author
VINCENT NYANDIRU
Software Engineer | Data Engineer
