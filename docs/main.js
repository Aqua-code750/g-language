document.addEventListener('mousemove', (e) => {
    const showcase = document.querySelector('.code-showcase');
    if(showcase) {
        const x = (window.innerWidth / 2 - e.pageX) / 50;
        const y = (window.innerHeight / 2 - e.pageY) / 50;
        showcase.style.transform = `perspective(1000px) rotateY(${x - 5}deg) rotateX(${y}deg)`;
    }
});
