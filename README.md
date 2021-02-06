
<!-- PROJECT LOGO -->
<br />
<p align="center">
  
  <h3 align="center">DigitalUniversity1.0
</h3>

  <p align="center">
    This Project is developed during the HackEd Hackathon,
to help all the students from class 1st to PhD, 
to get audio/video full transcription along with its summary and highlighted Keywords, 
to grasp everything quickly during examination.
Further, they can get the relevant material/books online and 
Timetable to join the online class, by just tapping the resp. subject!!


One of the sub feature of this project for transcription was used in hackathon CB2.0, which started after HackEd and ended before HackEd Hackathon.

To test the project Live - https://meeralin.github.io/DigitalUniversity1.0/home.html
    <br />
    <br />
    <a href="https://github.com/justafolk/Transcribo">View Demo</a>
    ·
    <a href="https://github.com/justafolk/Transcribo/issues">Report Bug</a>
    ·
    <a href="https://github.com/justafolk/Transcribo/issues">Request Feature</a>
  </p>
</p>







<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]
[![Product Name Screen Shot][product-screenshot1]]

Transcribo basically trascribes Online video lectures/meetings and adds highlights/topics related to content present in the source!
This project is can be useful in many interests.

For eg:
* If one needs keywords for their Yt video, they can use it for subtitles as well as for reach via topics.
* Students can use the returned document as reference or side notes for studying.
* It's tedious to just read a transcript of the words spoken, so it adds highlights to the content to be aware what part interests someone!

Of course, this project is at it's initial stage, but with more data and more model validation, it can turn out to be quite useful.


### Built With

This project is entirely based on Python. The following packages and Models were used:
* Scikit-Learn
* MoviePy and Pydub
* SpeechRegonition by Google
* Latent Dirchlett Allocation
* Numpy
* Gensim
* TfidVectorizer
* NTLK




<!-- GETTING STARTED -->
## Getting Started


### Prerequisites

I assume you are using either anaconda or Google colab for running the python notebooks.
* 
  ```sh
  pip install -r requirements.txt
  ```
or
Download the environment file for Anaconda prompt
```
https://drive.google.com/file/d/1mYBmfRa5E3BshmDhCVgsDhNcqoQOWqqr/view?usp=sharing
```
### Installation

Just add your video title and files_path variable, and you are good to go!



<!-- USAGE EXAMPLES -->
## System Implementation

Firstly the project is based on Flask, so all the data dealing is done by the
framework smoothly. The first real task of the program is to convert the
video file provided to an .wav audio file for transcription. We did this using
a package called moviepy. Then the output audio clip was gone through
Google’s Speech recognition API in a loop to cover the whole audio. The
transcription from the API was saved in a local .txt file for better use. We
tried to append the whole transcription to a single string, but we got some
runtime issues (Basically out of RAM). Though Google API is one of the
best speech Recognition API out there, it doesn’t punctuate the text in the
output. Thus, we came across a pre-trained punctuation model based on
theano and a package called “punctuator”. We punctuated our text with
the model itself. The summarization process: For getting the summary out
of the text, we went through several options, and chose Scikit learn’s
tfidfvectorizer. The process seems to be complicated but was quite easy.
First, dividing the text with sentences with the help of punctuations, then
tokenize each word with the help of nltk’s word_tokenise. Then getting
the average of frequency of words and removing stopwords/regular words
from the text. Then calculating the importance or Accuracy of the words in
the sentence. Then with that accuracy, calculate which sentences are
more valuable. Lastly, adding the sentences with the highest threshold to
the cut of final summary. And all the data we obtained from the following
system is given out as html with the help of Flask!



<!-- ROADMAP -->
## Applications
This project has wide range of applications, some of which are listed
below:-
1. For School/College Students, to get notes, if they missed any
class by chance.
2. For School/College Students, to get notes with highlighted
keywords, to revise the class during examinations.
3. For Business professionals to get the minutes of meeting.
4. For all the online events and workshops, which happens online,
and after that report is to be prepared.
5. To know the name of medicines and brief of call, when the
doctor consults the patients online using video/audio call.
6. To store the financial based startup’s (like policy bazaar) call data
in transcripted files, for future evidence and reference.
7. For all Specially abled who can’t hear the audio/video can see
the transcription.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Team - [@just_a_folk](https://twitter.com/just_a_folk) - 
       [@MeeraliN](https://github.com/MeeraliN)-






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: Images/ss.jpeg
[product-screenshot1]: Images/ss2.jpeg

