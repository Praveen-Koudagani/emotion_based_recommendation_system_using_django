const chatButton = document.querySelector('.chatbox__button');
const chatContent = document.querySelector('.chatbox__support');
const icons = {
    isClicked: /*'<img src="./images/icons/chatbox-icon.svg" />'*/'close',
    isNotClicked: /*'<img src="./images/icons/chatbox-icon.svg" />'*/'Error Reporting'
}
const chatbox = new InteractiveChatbox(chatButton, chatContent, icons);
chatbox.display();
chatbox.toggleIcon(false, chatButton);