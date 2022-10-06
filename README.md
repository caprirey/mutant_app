<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://w7.pngwing.com/pngs/559/527/png-transparent-wolverine-emma-frost-cyclops-beast-x-men-x-men-file-emblem-logo-computer-wallpaper.png" alt="Logo" width="120" height="70">
  </a>

<h3 align="center">Mutantes</h3>

  <p align="center">
    Search gene x in the dna chain
    <br />    
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>        
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>    
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Project that pretend to find the x gene in array nxn dimensions:

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* python
* fastapi
* boto3


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

For to get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python 3.9

### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
2. Install packages with pip
   ```sh 
   pip install -r requirements.txt
   ```
3. Create table "mutants" in AWS Dynamo DB with this settings:
   
   * Table details
    "Table name" -> "mutants"
    "Partition key" -> "id" data type String
   * Table settings -> Default settings  
  <br/>
   
4. Enter your aws API keys for dynamodb and table name in `/app/config/config.ini`
   
   ```sh
    aws_access_key_id = 
    aws_secret_access_key = 
    region_name = 
    table = mutants    
   ```

5. Run coverage test 
   
   ```sh
    coverage run -m pytest
   ```

6. Generate coverage report and html doc for more detail, the last command create one directory in the root named "htmlcov"
    ```sh
    coverage report    
   ```

    ```sh
    coverage html    
   ```

7. Run application whith 10 worker processes:
   ```
   uvicorn app.main:app --workers=10
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

The API exposes the following endpoints:

- [ ] Methods
  - [ ] POST - http://127.0.0.1:8000/api/v1/mutant/
    - [ ] Request example: 
      ```json
      {"dna":["ATGCGA","CCGTAC","TTAAGT","AGAAGG","CCCCTA","TCACTG"]}
      ```
    - [ ] Response example:
      ```json
      { "result": "you have gene x" }
      ```

  - [ ] GET
    - [ ] http://127.0.0.1:8000/api/v1/stats
    - [ ] Response example:
      ```json
      { "count_mutant_dna": 270, "count_human_dna": 396, "ratio": 0.7 }
      ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@caprirey](https://twitter.com/caprirey)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
