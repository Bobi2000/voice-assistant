# voice-assistant
<hr/>
<h3>The project consists of 2 main parts</h3>
<ul><b>1. Logic Part</b></ul>
<ul><b>2. UI Part</b></ul>
<hr/>

<h4>Logic Part</h4>
<p>
  The Logic part is the main app.
  It consists of:
  <ul><b> 1. IO </b></ul>
  <ul><b> 2. Commands </b></ul>
  <ul><b> 3. Interpetor for commands </b></ul>
</p>

<h4>IO</h4>
<ul>
 <b> Input </b> - Is provided by <b>Google's API</b> which takes the input from the microphone and then using an AI pattern to recognize the words.
</ul>
<ul>
 <b> Output </b> - Is provided by <b>pyttsx3</b> that takes a string and speaks it back to the user.
</ul>

<h4>Commands</h4>
<ul>
 <h5> A few commands for an example of what the assistant does: </h5>
</ul>

<ul>
 <b> GreetCommand </b> - Greets the User with an appropriate greeting by time.
</ul>

<ul>
  <b> JokeCommand </b> - Calls an JOKE API and tells you a random joke given by the API.  
</ul>

<ul>
  <b> OpenBrowserCommand </b> - Opens IE Edge and opens a specific website of your choosing.  
</ul>

<ul>
  <b> WolframalphaCommand </b> - Gives you the power of Wolframalpha API only by talking.
</ul>

<ul>
  <b> WindowsCommand </b> - Can lock or clean your recycle bin.
</ul>

<ul>
  <b> StoriesCommand </b> - Calls a random story by Aesop's Fables and tells you the moral of it.
</ul>

<h4>Interpetor for commands</h4>
<ul>
  The interpretor is given the input of the microphone and then it decides which command to execute by getting the most relevant one.  
</ul>

<hr/>

<h4>UI Part</h4>
<ul>
  UI was created by <b>tkinter</b> and <b>customtkinter</b>
  It consists of the main widget with a looping of images that generate a gif. To be played on the background while the app is running.
</ul>

<hr/>
