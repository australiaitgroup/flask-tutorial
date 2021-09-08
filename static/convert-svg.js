document.querySelectorAll('img.svg').forEach(svg => {
    const imgClass = svg.classList;
    const imgSrc = svg.src;

    fetch(imgSrc)
    .then(res => res.text())
    .then(newSvg => {
        let svgSpan = document.createElement('span');
        svgSpan.innerHTML = newSvg;

        svgSpan.querySelector('svg').classList.add(imgClass);
        svgSpan.querySelector('svg').removeAttribute('xmlns:a');
        svg.parentNode.replaceChild(svgSpan.firstChild, svg);
    })
})