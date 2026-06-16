<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<h1 align="center">CLI Calculator</h1>

  <p align="center">
    A small CLI Calculator written in Python.
    <br />
    <br />
    <a href="https://github.com/mh-tobi/CLI_Calculator/issues/new?labels=bug&template=bug_report.md">Report Bug</a>
    &middot;
    <a href="https://github.com/mh-tobi/CLI_Calculator/issues/new?labels=enhancement&template=feature_request.md">Request Feature</a>
  </p>



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
      <ul>
        <li><a href="#calculate">calculate</a></li>
        <li><a href="#menu">menu</a></li>
      </ul>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

In this project, I attempted to create a simple CLI calculator using Python.
The primary goal was to expand my portfolio and improve my Python skills.

To ensure robust CLI functionality, the Python library Click was utilized.
Click enables the creation of composable and intuitive command-line interfaces with minimal code.
One of the key advantages of this library is the automatic generation of help pages (--help).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python.org]][Python-url]
  * [Click](https://click.palletsprojects.com/en/stable/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Python >=3.14

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/MH-Tobi/CLI_Calculator.git
   ```
2. Move into the CLI_Calculator folder
   ```sh
   cd ./CLI_Calculator
   ```
3. Create a virtual environment
   ```sh
   python -m venv venv
   ```
4. Activate the virtual environment
   ```sh
   ./venv/Scripts/activate
   ```
5. Install the library (-e for the editable variant)
   ```sh
   python -m pip install -e .
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### calculate

To execute a calculation you have to use the `calculate`-argument like.
```sh
calculator calculate -- 2+3*4/-2
```

The double hyphens `--` are only required if the first number has a negative value. Like:
```sh
calculator calculate -- -54/22
```

In this case, Click attempts to interpret the expression as an option. This can be bypassed using double hyphens.

The calculator maintains a history.
This makes it possible to incorporate the most recently generated result into a new calculation.
This is achieved by using the keyword `res`.
```sh
calculator calculate -- res*5
```

If no history has yet been created, a value of 0 is assumed for `res`.

In addition to the previous result, constants can also be incorporated into the calculation.
This allows for the use of both predefined constants —such as `pi`— and user-defined constants.
```sh
calculator calculate -- pi+17
```

```sh
calculator calculate -- self-22
```

In addition to integers, real numbers may, of course, also be used.
A `.` must be used as the decimal separator.
```sh
calculator calculate -- -3.74*0.344-22.00001+2.1/4.43
```

#### Rules for calculation

- Numbers must have the format `[+\-]?[0-9]+\.?[0-9]*` (For an explanation, see page [regex101](https://regex101.com/)).
- There may be only one operator between two numbers. (Allowed operators are `+`, `-`, `*`, `/`)
- Keywords must not be negated using a leading minus sign. (To negate them, use `*-1`)
- Spaces can be used to separate numbers and operators. (like `-2 * -5 / 2 + 1`)
- Parenthesis Pairs for Encapsulating Expressions. (like `(2+4)*(3+2)`)

#### Examples

- allowed:
  - `calculator calculate -- -2+-2` = `-4`
  - `calculator calculate -- 2.35  * 2.1` = `4.935`
  - `calculator calculate -- res - -2` = `2` (when `res`= 0)
  - `calculator calculate -- pi *     sierpinski` = `8.1209597056`
- not allowed:
  - `calculator calculate -- -2---2` => `---2` too many characters
  - `calculator calculate -- -res+2` => `-res` negated Keyword
  - `calculator calculate -- res^4` => `^` currently unallowed operator
  - `calculator calculate -- 2,4 * 2` => The decimal separator is a `,` instead of a `.`.
  - `calculator calculate -- (2.4 * 2)(5/3)` => Missing Operator between the two parenthesis pairs

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### menu

Settings can be configured and lists generated via the `menu`-argument.

Specific options are used for this purpose.

#### --get-history

This option allows the history to be output.
```sh
calculator menu --get-history
```

#### --clean-history

With this option, the entire history can be deleted.
```sh
calculator menu --clean-history
```

#### --get-variables

This option allows you to output all user-defined constants.
```sh
calculator menu --get-variables
```

#### --set-variable <name, value>

With this option, a constant can be created manually.
```sh
calculator menu --set-variable alpha 15
```

#### --delete-variable <name>

This option allows you to remove a specific user-defined constant.
```sh
calculator menu --delete-variable alpha
```

This option can also be specified multiple times.
```sh
calculator menu --delete-variable alpha --delete-variable beta --delete-variable gamma
```

#### --clean-variables

With this option, all user-created constants can be removed.
```sh
calculator menu --clean-variables
```

#### --get-constants

With this option, all predefined constants can be output.
```sh
calculator menu --get-constants
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Detection of Parenthesis Pairs for Encapsulating Expressions
- [ ] Extension of Operators
  - [ ] Powers (^ or **)
  - [ ] Modulo (%)
- [ ] Complete the help

See the [open issues](https://github.com/MH-Tobi/CLI_Calculator/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/MH-Tobi/CLI_Calculator/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=MH-Tobi/CLI_Calculator" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the MIT license. See '[LICENSE](/LICENSE)' for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/MH-Tobi/CLI_Calculator](https://github.com/MH-Tobi/CLI_Calculator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/MH-Tobi/CLI_Calculator.svg?style=for-the-badge
[contributors-url]: https://github.com/MH-Tobi/CLI_Calculator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/MH-Tobi/CLI_Calculator.svg?style=for-the-badge
[forks-url]: https://github.com/MH-Tobi/CLI_Calculator/network/members
[stars-shield]: https://img.shields.io/github/stars/MH-Tobi/CLI_Calculator.svg?style=for-the-badge
[stars-url]: https://github.com/MH-Tobi/CLI_Calculator/stargazers
[issues-shield]: https://img.shields.io/github/issues/MH-Tobi/CLI_Calculator.svg?style=for-the-badge
[issues-url]: https://github.com/MH-Tobi/CLI_Calculator/issues
[license-shield]: https://img.shields.io/github/license/MH-Tobi/CLI_Calculator.svg?style=for-the-badge
[license-url]: https://github.com/MH-Tobi/CLI_Calculator/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/tobias-pflug
[product-screenshot]: images/screenshot.png
<!-- Shields.io badges. You can find a comprehensive list with many more badges at: https://github.com/inttter/md-badges -->
[Python-url]: https://www.python.org/
[Python.org]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff
