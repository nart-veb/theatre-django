// Change Language

const langOne = document.querySelector(".langButtonOne");
const langTwo = document.querySelector(".langButtonTwo");
langOne.addEventListener("click", (e) => {
  e.preventDefault();
  langOne.classList.add("activeLang");
  langTwo.classList.remove("activeLanguage");
});

langTwo.addEventListener("click", (e) => {
  e.preventDefault();
  langTwo.classList.add("activeLanguage");
  langOne.classList.remove("activeLang");
});

// burgerButton

const burgerContainer = document.querySelector(".burger_menu");
const burgerButton = document.querySelector(".burgerButton");
const burgerButtonAlt = document.querySelector(".burgerButtonAnother");
burgerButton.addEventListener("click", (e) => {
  e.preventDefault();
  burgerContainer.classList.add("activeBurger");
});
burgerButtonAlt.addEventListener("click", (e) => {
  e.preventDefault();
  burgerContainer.classList.add("activeBurger");
});

// closeBurgerBtn

const closeBurger = document.querySelector(".burgerCloseBtn");

closeBurger.addEventListener("click", (e) => {
  e.preventDefault();
  burgerContainer.classList.remove("activeBurger");
});

window.onload = () => {
  let url = window.location.href;
  $.ajax({
    url: `${url}get-map/`,
    method: "get",
    datatype: "html",
    data: {},
    success: function (map_url) {
      $.ajax({
        url: "http://127.0.0.1:8000" + map_url,
        method: "get",
        datatype: "xml",
        data: {},
        success: function (svg) {
          var dataSvg = $(svg).find("svg");
          $(".place_map").append(dataSvg.clone());
          $.ajax({
            url: `${url}get-tickets/`,
            method: "get",
            datatype: "json",
            data: {},
            success: function (tickets) {
              init_map(tickets);
            },
          });
        },
      });
    },
  });
};

function init_map(tickets) {
  tickets.forEach((ticket) => {
    seat = document.querySelector(
      `circle[data-seat-id='${ticket["fields"]["seat_id"]}']`
    );
    seat.classList.add("open");
    seat.setAttribute("data-ticket-id", ticket["pk"]);
    seat.setAttribute("data-event-id", ticket["fields"]["poster"]);
    seat.setAttribute("data-row-number", ticket["fields"]["row_number"]);
    seat.setAttribute("data-seat-number", ticket["fields"]["seat_number"]);
    seat.setAttribute("data-price", ticket["fields"]["price"]);
    seat.setAttribute("data-sector", ticket["fields"]["sector"]);
  });
  const svg = document.querySelector("svg");
  const panzoom = svgPanZoom(svg, {
    zoomScaleSensitivity: 0.5,
  });
  window.addEventListener("resize", () => {
    panzoom.resize();
    panzoom.fit();
    panzoom.center();
  });
  const control_minus = document.querySelector(".control_minus");
  const control_plus = document.querySelector(".control_plus");
  control_minus.addEventListener("click", () => {
    panzoom.zoomOut();
  });
  control_plus.addEventListener("click", () => {
    panzoom.zoomIn();
  });
  $(".loader")[0].classList.remove("active");
}
