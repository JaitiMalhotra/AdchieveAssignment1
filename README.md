# Project Description

* REST API to calculate the distance from given list of addresses to Adchieve HQ, sorts them and stores in a CSV which can be applied through localhost/api/v1/distances

    ### Unit Testing Framework
    * This project was developed in an iterative development cycle that emphasizes writing automated tests before writing the actual code, also known as Test Driven Development(TDD) approach.
      
    * To test APIs, we use the same existing Django test framework, but with added support of DRF's helper classes. These classes extend Django's existing classes.

## Prerequisites

* Git
* Python3
* Virtualenv

## Setup

* Create a virtualenv using python3 `python3 -m venv env-name`

* Activate the virtualenv  `source env-name/bin/activate`

* Clone the repository `git clone git@git.easternenterprise.com:jaitimalhotra/adchieveassignment.git`  

* Install all the dependencies inside your virtualenv `pip3 install -r requirements.txt` 

## Running Django Server
* Start local server- `python manage.py runserver`

# Input

* Input is a list of name and address of the location in this format.

`[
        {
            "name": "Eastern Enterprise B.V.",
            "address": "Deldenerstraat 70, 7551AH Hengelo, The Netherlands"
        },
        {
            "name": "Eastern Enterprise",
            "address": "46/1 Office no 1 Ground Floor , Dada House , Inside dada silk mills compound, Udhana Main Rd, near Chhaydo Hospital, Surat, 394210, India"
        },
        {
            "name": "Adchieve Rotterdam",
            "address": "Weena 505, 3013 AL Rotterdam, The Netherlands"
        },
        {
            "name": "Sherlock Holmes",
            "address": "221B Baker St., London, United Kingdom"
        },
        {
            "name": "The White House",
            "address": "1600 Pennsylvania Avenue, Washington, D.C., USA"
        },
        {
            "name": "The Empire State Building",
            "address": "350 Fifth Avenue, New York City, NY 10118"
        },
        {
            "name": "The Pope",
            "address": "Saint Martha House, 00120 Citta del Vaticano, Vatican City"
        },
        {
            "name": "Neverland",
            "address": "5225 Figueroa Mountain Road, Los Olivos, Calif. 93441, USA"
        }
    ]
`

# Usage

* API for calculating distance is:
`localhost/api/v1/distance/`

* POST the input json of addresses in the above format. 

* Output will be stored in the Project directory as 'distance.csv' as well shown on console and in API response