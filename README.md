# indic-python
 The python language for Indian Languages

## Purpose
Python is a very versatile language and can be used everywhere. I recently came across an ad of a company which was teaching Python in indic languages. So there was a teacher who was teaching the syntax of the Python language in kannada, and I was thinking, "This is nuts! You still have to know English to understand what the keywords mean!" That is when it clicked to me about a python language written in indic languages.

This project is still under development. I have no Idea on where to start, how to do. I have done a basic job of replacing occurances, but I am sure, there is more to it!

So, feel free to contribute! Let's make this something nice to learn! Let's show everyone that we can code in any Indian Language!

## Story

I got this idea when I was talking to my mother. Here is a snippet of our convo

Mum: See this! This company is teaching coding in kannada!

Me: Yeah, I know this. It's been there since a while now.

Mum: Isn't this nice! People can learn coding in their mother tongues!

Me: Yeah, it seems nice, but they still have to learn english as the keywords are written in english. If the keywords were in their local languages, then it made sense. 

That got me thinking, "Why isn't there such a thing? There should be one!" I didn't know if this was needed or not. I still don't! I feel it's stupid. But, I love to code, I had time... So, why not?

Later during the day, I stumbled across Bhailang. No explanation needed. I had to do it.

I know, this might seem stupid. But, it doesn't harm to have a indic python, right?
I learnt lots of things while building this, so no regrets!

## Usage
### Downloading indicpy
You can use pip to install indicpy.
```shell
pip install indicpy
```

You can also download the repository and install using the setup.py file. However, pip is recommended as it is easy.

### Creating a indic python file.
Create a file using the file extension py```[xx]``` or py```[xxx]```  where ```xx``` or ```xxx``` is the 2 letter and 3 letter ISO Code for the indic language respectively.

You can also use the file extension epy```[xx]``` or epy```[xxx]``` for indic-python written in english alphabet but conforms to the indic language keywords.

Example - kannada.pykn, hindi.pyhi

### Writing code in the indic language.
The syntax of the indic python is same as normal python. Just replace the keywords with the indic ones. The indic keywords are present in keywords/```[language]```.yml

### Examples
To see some simple examples, check out the examples folder.

### Running the program.
You can run a file called ```indic_file.pyxx``` using the following command.
```shell
py -m indicpy indic_file.pyxx
```

Here's an example. You can run a sample code written in kannada using the following command
```shell
py -m indicpy examples/kannada.pykn
```
