import random
import speech_recognition as sr


def speech_engine(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_sphinx(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":

    WAKE = "anaconda"

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(device_index=5) # My Snowball mic usually sits at this index on my machine. You can change it, or remove this
   
    print('You have the following microphones available: ' + str(sr.Microphone.list_microphone_names()))

    print("I'm waiting for a command. Speak!")

    human_input = speech_engine(recognizer, microphone)

    if human_input["error"]:
        print("ERROR: {}".format(human_input["error"]))

    # show the user the transcription
    if WAKE == human_input["transcription"]:
        print("Wow I got the wake phrase right! I'm such a clever computer! The wake phrase is: {}".format(WAKE))
    else:
        print("You said: {}".format(human_input["transcription"]))

