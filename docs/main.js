// Copy to clipboard functionality
function copyInstallCmd() {
    const cmd = "echo \"Set-Alias -Name g -Value 'C:\\Users\\kavs1\\OneDrive\\Desktop\\a language\\dist\\g.exe'\" >> $PROFILE";
    navigator.clipboard.writeText(cmd).then(() => {
        const btn = document.querySelector('.copy-btn');
        btn.innerText = "Copied!";
        btn.style.background = "#27c93f";
        setTimeout(() => {
            btn.innerText = "Copy";
            btn.style.background = "";
        }, 2000);
    });
}

// 3D Parallax effect on code showcase
document.addEventListener('mousemove', (e) => {
    const showcase = document.querySelector('.code-showcase');
    if(showcase && window.innerWidth > 900) {
        const x = (window.innerWidth / 2 - e.pageX) / 40;
        const y = (window.innerHeight / 2 - e.pageY) / 40;
        showcase.style.transform = `perspective(1000px) rotateY(${x}deg) rotateX(${y}deg) translateY(-5px)`;
    }
});

// Typewriter effect for Hero section
const words = ["English.", "easier.", "faster.", "intuitive.", "fun again."];
let i = 0;
let timer;

function typingEffect() {
    let word = words[i].split("");
    var loopTyping = function() {
        if (word.length > 0) {
            document.getElementById('typewriter').innerHTML += word.shift();
        } else {
            setTimeout(deletingEffect, 2000);
            return false;
        }
        timer = setTimeout(loopTyping, 100);
    };
    loopTyping();
}

function deletingEffect() {
    let word = words[i].split("");
    var loopDeleting = function() {
        if (word.length > 0) {
            word.pop();
            document.getElementById('typewriter').innerHTML = word.join("");
        } else {
            if (words.length > (i + 1)) {
                i++;
            } else {
                i = 0;
            }
            typingEffect();
            return false;
        }
        timer = setTimeout(loopDeleting, 50);
    };
    loopDeleting();
}

// Add cursor blinking element
document.addEventListener("DOMContentLoaded", () => {
    const typewriterElement = document.getElementById('typewriter');
    if (typewriterElement) {
        const cursor = document.createElement('span');
        cursor.className = 'typewriter-cursor';
        typewriterElement.parentNode.insertBefore(cursor, typewriterElement.nextSibling);
        typingEffect();
    }
    
    // Intersection Observer for scroll animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.feature-card, .module-item').forEach(el => {
        el.style.opacity = "0";
        el.style.transform = "translateY(30px)";
        el.style.transition = "all 0.6s ease-out";
        observer.observe(el);
    });
});
