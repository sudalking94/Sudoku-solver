function seletNumber(id) {
  const tdId = document.getElementById(id);
  tdId.style.backgroundColor = "skyblue";
  tdId.setAttribute("selected", true);
}

function completeRest() {
  const data = document.getElementsByClassName("data");
  Array.prototype.forEach.call(data, function (v) {
    v.textContent = 0;
    v.style.backgroundColor = "unset";
    hoverHandler(v);
  });
}

function setNumber(text) {
  const datas = document.getElementsByClassName("data");
  const selectedData = [...datas].filter(
    (value) => value.getAttribute("selected") === "true"
  );
  Array.prototype.forEach.call(selectedData, function (v) {
    v.textContent = text;
    v.style.backgroundColor = "unset";
    v.setAttribute("selected", false);
    hoverHandler(v);
  });
}

function hoverHandler(v) {
  v.addEventListener("mouseenter", function () {
    v.style.backgroundColor = "skyblue";
  });
  v.addEventListener("mouseleave", function () {
    v.style.backgroundColor = "unset";
  });
  v.addEventListener("click", function () {
    v.style.backgroundColor = "skyblue";
    v.addEventListener("mouseleave", function () {
      v.style.backgroundColor = "skyblue";
    });
  });
}

function submitHandler() {
  const data = document.getElementsByClassName("data");
  const dataList = {};
  Array.prototype.forEach.call(data, function (obj, i) {
    dataList[i] = obj.textContent;
  });
  fetch(`/result`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dataList),
  });
}
