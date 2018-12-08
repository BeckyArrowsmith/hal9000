# hal9000

Adventures in Speech Recognition!

I want build my own Personal Assistant that will live on a Raspberry Pi. As you've probably guessed from the repo name, this will be HAL9000 themed.

This is just a bit of a spike into various speech processing libraries and APIs.

## PyAudio & PortAudio

[PyAudio](http://people.csail.mit.edu/hubert/pyaudio/#downloads) is required if you want to use microphone input (Microphone).

Portaudio can be installed with `brew install portaudio`

## The Recognizer instance

The Recognizer instance in the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library has multiple methods for recognising speech from an audio source using various APIs. Google is the most common, but here I'm using [Pocketsphinx](https://github.com/bambocher/pocketsphinx-python) because I want to keep selfhosted. See the CMU Sphinx section for more information.

## CMU Sphinx

 You will need to install the [CMU Sphinx engine onto your machine](https://cmusphinx.github.io/wiki/tutorialoverview/). I ran into a lot of difficulties using the instructions there (it involves building from source) but I had great success following the instructions [here](http://www.moreiscode.com/getting-started-with-cmu-sphinx-on-mac-os-x/), using brew instead. If you follow that blog post, ensure you give yourself time to update Xcode - it takes bloody forever.

### Other stuff

Sphinx seems pretty terrible and the Google API is much better (I haven't tried the others). Alas, I don't want data up on the evil cloudz so I'll perservere and learn if I can make Sphinx better.

The wake word `anaconda` is purely chosen because it's hard to get wrong. But at the moment, this app does still get it wrong 🙃. Ideally, my wake phrase would be "Hey HAL" but that is being transcribed as anything from "e how" to "no" (yeah lol). It'll get better as I learn how to reduce noise and improve accuracy.