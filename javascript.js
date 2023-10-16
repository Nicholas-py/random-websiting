
function celebrate() {
  document.getElementById("hiddenMessage").style.display = 'block';
  document.getElementById('agreeButton').innerHTML = 'Agree';

}

function textholderloaded() {
  var globaltext = localStorage.getItem('gobacktext');
  document.getElementById('showuptext').innerHTML = globaltext;
  }


function moreButtoning() {
  document.getElementById("hiddenMessage").style.display = 'none';
  document.getElementById('agreeButton').innerHTML = 'You don\'t need to do it again';
}

function uselessSubmitted() {
  document.getElementById('goback').style.display = 'block'
  var text = document.getElementById('Textbox').value;
  oldtext = localStorage.getItem('gobacktext');
  if (oldtext == null) {
    localStorage.setItem('gobacktext', text)
  } else {
    localStorage.setItem('gobacktext',oldtext + text);
  }
  
}
