
<div align="center">
  <img src="https://blogs.cappriciosec.com/uploaders/tools-banner.png" alt="logo">
</div>


## Badges



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![PyPI - Version](https://img.shields.io/pypi/v/crlfi)
![PyPI - Downloads](https://img.shields.io/pypi/dm/crlfi)
![GitHub all releases](https://img.shields.io/github/downloads/Cappricio-Securities/crlfi/total)
<a href="https://github.com/Cappricio-Securities/crlfi/releases/"><img src="https://img.shields.io/github/release/Cappricio-Securities/crlfi"></a>![Profile_view](https://komarev.com/ghpvc/?username=Cappricio-Securities&label=Profile%20views&color=0e75b6&style=flat)
[![Follow Twitter](https://img.shields.io/twitter/follow/cappricio_sec?style=social)](https://twitter.com/cappricio_sec)
<p align="center">

<p align="center">







## License

[MIT](https://choosealicense.com/licenses/mit/)



## Installation 

1. Install Python3 and pip [Instructions Here](https://www.python.org/downloads/) (If you can't figure this out, you shouldn't really be using this)

   - Install via pip
     - ```bash
          pip install crlfi
        ```
   - Run bellow command to check
     - `crlfi -h`

## Configurations 
2. We integrated with the Telegram API to receive instant notifications for vulnerability detection.
   
   - Telegram Notification
     - ```bash
          crlfi --chatid <YourTelegramChatID>
        ```
   - Open your telegram and search for [`@CappricioSecuritiesTools_bot`](https://web.telegram.org/k/#@CappricioSecuritiesTools_bot) and click start

## Usages 
3. This tool has multiple use cases.
   
   - To Check Single URL
     - ```bash
          crlfi -u http://example.com 
        ```
   - To Check List of URL 
      - ```bash
          crlfi -i urls.txt 
        ```
   - Save output into TXT file
      - ```bash
          crlfi -i urls.txt -o out.txt
        ```
   - Want to Learn about [`crlfi`](https://blogs.cappriciosec.com/blog/138/Cappricio%20Securities%20Discovers%20CRLF%20Injection%20Vulnerability%20in%20Popular%20Website,%20Responsible%20Disclosure%20Earns%20Bounty)? Then Type Below command
      - ```bash
          crlfi -b
        ```
     
<p align="center">
  <b>🚨 Disclaimer</b>
  
</p>
<p align="center">
<b>This tool is created for security bug identification and assistance; Cappricio Securities is not liable for any illegal use. 
  Use responsibly within legal and ethical boundaries. 🔐🛡️</b></p>


## Working PoC Video

[![asciicast](https://blogs.cappriciosec.com/uploaders/Screenshot%202024-04-23%20at%203.45.51%20PM.png)](https://asciinema.org/a/aqBLIxq5XfyWH7hiHPNouCcKZ)




## Help menu

#### Get all items

```bash
👋 Hey Hacker
                                v1.0
   __________  __    __________
  / ____/ __ \/ /   / ____/  _/
 / /   / /_/ / /   / /_   / /
/ /___/ _, _/ /___/ __/ _/ /
\____/_/ |_/_____/_/   /___/

                                Developed By https://cappriciosec.com


crlfi : Bug scanner for WebPentesters and Bugbounty Hunters 

$ crlfi [option]

Usage: crlfi [options]
```


| Argument | Type     | Description                | Examples |
| :-------- | :------- | :------------------------- | :------------------------- |
| `-u` | `--url` | URL to scan | crlfi -u https://target.com |
| `-i` | `--input` | filename Read input from txt  | crlfi -i target.txt | 
| `-o` | `--output` | filename Write output in txt file | crlfi -i target.txt -o output.txt |
| `-c` | `--chatid` | Creating Telegram Notification | crlfi --chatid yourid |
| `-b` | `--blog` | To Read about crlfi Bug | crlfi -b |
| `-h` | `--help` | Help Menu | crlfi -h |



## 🔗 Links
[![Website](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://cappriciosec.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/karthikeyan--v/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/karthithehacker)



## Author

- [@karthithehacker](https://github.com/karthi-the-hacker/)



## Feedback

If you have any feedback, please reach out to us at contact@karthithehacker.com
