$(document).ready(function(){
    $('.customer-logos').slick({
        slidesToShow: 6,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 1500,
        arrows: false,
        dots: false,
        pauseOnHover: false,
        responsive: [{
            breakpoint: 768,
            settings: {
                slidesToShow: 4
            }
        }, {
            breakpoint: 520,
            settings: {
                slidesToShow: 3
            }
        }]
    });
});



const content = [
    {
        title: 'Item 1',
        body: 'This is the content for item 1.'
    },
    {
        title: 'Item 2',
        body: 'This is the content for item 2.'
    },
    {
        title: 'Item 3',
        body: 'This is the content for item 3.'
    },
    {
        title: 'Item 4',
        body: 'This is the content for item 4.'
    },
];

function showContent(index) {
    const sidebarItems = document.querySelectorAll('.sidebar li');
    const contentTitle = document.querySelector('.content h1');
    const contentBody = document.querySelector('.content p');

    // remove active class from all items
    sidebarItems.forEach((item) => {
        item.classList.remove('active');
    });

    // add active class to selected item
    sidebarItems[index].classList.add('active');

    // set content
    contentTitle.innerText = content[index].title;
    contentBody.innerText = content[index].body;
}