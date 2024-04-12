# AI_Helper
AI_Helper for Budget diary with voice control to provide analytic and AI-accitent.

## Components
1. Script for speech-to-text recognition: <br>input - data from micro (maybe recorded into temp file and provide to input) and language; <br> output: parced text (maybe later I'll add punctuation to recognised text)
2. Bunch of scripts for AI-assistante: <br>
    2.1. Assitance for converting input parced speech into set of predefined commands (NN as classifyer into commands)<br>
    2.2. Assitance to fill the budget diray: if the recognised text contains key words - then analyse it and convert input speeach into json file to fill budget table<br>
    2.3. Chat-bot: based on commands and provided from APP (c# budget analytics app) it will provide the requested answer in appropriate and comfortable form (dialogue)<br>
    2.4. Text-to-voice: voice response from chat bot<br>
3. Scipts to collect data (parcing screen for faster data collection for NN fine-tuning): they will not be included into exe NN helper for c# app
4. Scripts for NN fine-tuning: for the beggining I'll use JetMoE