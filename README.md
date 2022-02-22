# GitHub Profile Scraper

## Steps

1. Create folder **/data**
2. Download the page and save it as **.html** in folder **/data**
3. run [parser_people_list.py](parser_people_list.py)

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [GitHub Profile Scraper](#github-profile-scraper)
  - [Table of Contents](#table-of-contents)
  - [About the Project](#about-the-project)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Usage](#usage)
      - [User details](#user-details)
      - [Repository details](#repository-details)
      - [Commit details](#commit-details)
  - [Goals](#goals)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)
## About the Project

- A simple tool to fetch user details of a GitHub profile.
- It is built on top of [GitHub API v3](https://developer.github.com/v3/).
- Data is stored and manipulated in form of JSON.
- The data which can be grouped into 3 types, each with a different program and a python class.

  - **User Data** that contains user stats such 'Name', 'Location', 'Email', 'Followers' etc.
    Also stores a **Repository** list of the user.

  - **Repo Data** is used to collect data about a particular repository, such as 'number of forks', 'number of commits' etc.
  - **Commit Data** can be used to scrape commit history and 'Sha' values along with commit message.


<!-- LICENSE -->
## License

Distributed under the GPL-3.0 License. See `LICENSE` for more information.


## Next

- GitHub API blocks me (max 60 requests per hour)
> curl -I https://api.github.com/users/mab-az

- create a folder with all users individual profiles