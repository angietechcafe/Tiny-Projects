const quoteContainer = document.getElementById('quote-container'); 
const quoteText = document.getElementById('quote'); 
const authorText = document.getElementById('author'); 
const twitterBtn = document.getElementById('twitterbird'); 
const newQuoteBtn = document.getElementById('brand-new-quote'); 
//const loader = document.getElementById('loader');

let apiQuotes = []; //store quotes from API here via array

///Display Loading
//function loading () {
 //   loader.hidden = false; //hiding our div
 //   quoteContainer.hidden = true; //don't want to hide anything here
//}

//Hide Loading
//function complete () {
//    quoteContainer.hidden = false;
 //   loader.hidden = true;
//}

//Show New Quote Here
function newQuoteHere () {
    //Pick random quote here from the apiQuotes array
    const quote = apiQuotes[Math.floor(Math.random() * apiQuotes.length)];
    //Check if author field is blank and replace it with "Unknown"
    if (!quote.author) {
        authorText.textContent = "Unknown";
    } else {
        authorText.textContent = quote.author;
    }
    //Check quote length to determine styling
    if (quote.text.length > 115){
        quoteText.classList.add('long-quote');
    } else {
        quoteText.classList.remove('long-quote');
    }
    quoteText.textContent = quote.text; 

}
// Get quotes from API
async function getQuotesHere () { 
    const apiURL = 'https://type.fit/api/quotes';
        try {
            const response = await fetch(apiURL);
            apiQuotes = await response.json();
            newQuoteHere();
            console.log(apiQuotes[12]); 
         } catch (error) {
    //Debug error here by catching it.
    }
}

//Tweet Quote Here
function tweetQuoteHere() {
    const twitterURL = `https://twitter.com/intent/tweet?text=${quoteText.textContent} - ${authorText.textContent}`;
    window.open(twitterURL, '_blank');
}

//Event Listeners
newQuoteBtn.addEventListener('click', newQuoteHere);
twitterBtn.addEventListener('click',tweetQuoteHere);

//on load to ensure getQuotesHere fn works
getQuotesHere();
//newQuoteHere();

