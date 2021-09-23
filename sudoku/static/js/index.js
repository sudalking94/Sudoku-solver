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

async function submitHandler() {
  const data = document.getElementsByClassName("data");
  const dataList = [];

  await Array.prototype.forEach.call(data, function (obj, i) {
    dataList.push(obj.textContent);
  });
  const { board } = await fetch(`/result`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dataList),
  })
    .then((res) => res.json())
    .then((data) => data);

  board.forEach((eachArray, x) => {
    eachArray.forEach((e, y) => {
      const td = document.getElementById(x * 9 + y + 1);
      td.textContent = e;
    });
  });
}
