// Open the menu by display the
function openNav() {
    document.getElementById("myNav").style.width = "100%";
}

function closeNav() {
    document.getElementById("myNav").style.width = "0%";
}


/** Make navigation labels disapear when scrolling down */
// get client screen height
const screenHeight = window.innerHeight;
// listen for scrolling
window.addEventListener("scroll", function(event) {
    let windowHeight = window.pageYOffset;
    visible = true;

    if (windowHeight > screenHeight-100) {
        visible = false;
    } else {
        visible = true;
    }

    toggleNavButtons(visible);
}, false);

// toggle label visibility
function toggleNavButtons(visible) {
    if (visible) {
        document.getElementById("about").style.visibility = "visible";
        document.getElementById("team").style.visibility = "visible";
        document.getElementById("contact").style.visibility = "visible";

        document.getElementById("navButton").style.float = "none";

        document.getElementById("homeBt").style.visibility = "hidden";
        document.getElementById("homeBt").style.float = "none";
    }
    else {
        document.getElementById("about").style.visibility = "hidden";
        document.getElementById("team").style.visibility = "hidden";
        document.getElementById("contact").style.visibility = "hidden";

        document.getElementById("navButton").style.float = "right";
        document.getElementById("navButton").style.margin = "10px 40px 0 0";

        document.getElementById("homeBt").style.visibility = "visible";
        document.getElementById("homeBt").style.float = "left";
    }
}
