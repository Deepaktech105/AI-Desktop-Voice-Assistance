#No module named 'pyaudio'
For some reason pip does not work, instead you could try first installing "pipwin" if you don't already have it Open a cmd and paste this:

```
pip install pipwin
```

and then install PyAudio using:

```
pipwin install pyaudio
```

It should work. But if you don't want to use pipwin.. just install it and then uninstall it afterwards by simply using:

```
pip uninstall pipwin
```