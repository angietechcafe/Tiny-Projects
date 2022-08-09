<h1>How to make a pull request?</h1>

<h2>There are a series of steps that GitHub users can use to make a pull request. A common way of making a pull request is by using git commands from the terminal. In this tip document, I will mention how to do pull requests on a Mac terminal.</h2>
 
<h3>Install git</h3>
<p>People can install git on their computers by first installing homebrew. Afterwards, they can go on the terminal and type this brew command:
  $ brew install git</p>
    
<h3>Create a directory</h3>
<p>On the terminal, make a new directory using the mkdir command with a name. For example, we can make a directory with "mkdir project" . Next, create a file such as an HTML file that you want to update on your GitHub site.  If there is a mistake in the file, no worries. - We can update it by doing a pull request. However, before we do a pull request we need to create a branch aside from our main branch. </p>
   
<h3>Git branch, checkout, checkout -b commands</h3>
<p>Git branch command is used to develop, list, and delete branches. However, it is not permitted to change between branches or place a pasted forked come together once again.</p>
  
<h3>Git git add “filename.ext”</h3>
    <!--p-->
   
<h3>Git Status</h3>
    <!--p-->
    
<h3>git commit -m “put a message here”</h3>
  <!--p-->
    
<h3>git fetch upstream </h3>
    <!--p-->
  
<h3>git push --set-upstream origin "branch"</h3>
  <!--p-->
  
<h3>git checkout -b upstream-<directory> --track upstream/<directory></h3>
  <!--p-->
  
<h3>git pull</h3>
 <p>When in doubt, always update your local repository before you do a pull request. It will save you time and avoid merge conflicts.</p>
  
<h3>git push</h3>
 <!--p-->
