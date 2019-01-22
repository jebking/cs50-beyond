let drawing = false;
let radius = 5;
let red = 0;
let green = 0;
let  = 0;

document.addEventListener('DOMContentLoaded', () => {

    const canvas = d3.select('#canvas');

    canvas.on('mousemove', draw_point);

    canvas.on('mousedown', () => {
        drawing = true;
    });
    
    canvas.on('mouseup', () => {
        drawing = false;
    });
    
    canvas.on('mouseclick', draw_point);

    update_preview();
});

function draw_point() {
    if (!drawing) {
        return;
    }
    const coords = d3.mouse(this);

    const canvas = d3.select('#canvas');

    canvas.append('circle')
        .attr('cx', coords[0])
        .attr('cy', coords[1])
        .attr('r', radius)
        .style('fill', `rgb(${red},${green},${blue})`);
}

function erase() {
    const canvas = d3.select('#canvas');
    canvas.selectAll("*").remove();
}

function update_preview() {
    const preview = d3.select('#brush-preview');
    preview.selectAll("*").remove();

    let radius_el = document.querySelector('#size-slider');
    radius = radius_el.value;
    red = document.querySelector('#red-slider').value;
    green = document.querySelector('#green-slider').value;
    blue = document.querySelector('#blue-slider').value;

    preview.append('circle')
           .attr('cx', 30)
           .attr('cy', 30)
           .attr('r', radius)
           .attr('fill', `rgb(${red},${green},${blue})`);
}
