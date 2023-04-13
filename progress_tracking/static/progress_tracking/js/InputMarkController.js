const valid_var = ["5", "1", "2", "3", "4", "n"];

const inputs = document.querySelectorAll(".mark_input");
let changes = [];
const path = window.location.pathname.split("/").splice(2, 2);

inputs.forEach((input) => {
  input.addEventListener("input", (e) => {
    let valid = false;
    const new_stud_id = input.parentElement.parentElement.id;
    const new_date = input.parentElement.id;

    const result = changes.findIndex(
      ({ user_id, date }) => user_id === new_stud_id && date === new_date
    );

    if (result > -1) {
      if (e.target.value == "") changes.splice(result, 1);
    } else {
      valid_var.forEach((element) => {
        if (element == e.target.value) valid = true;
      });

      if (!valid) e.target.value = "";
      else {
        changes.push({
          mark: e.target.value,
          stud_id: new_stud_id,
          date: new_date,
        });
      }
    }
  });
});

const save_button = document.getElementById("saveBtn");
var csrftoken = document.cookie
  .split("; ")
  .find((row) => row.startsWith("csrftoken="))
  ?.split("=")[1];

save_button.onclick = () => {
  if (changes.length > 0) {
    let xhr = new XMLHttpRequest();
    xhr.responseType = "json";
    xhr.open("POST", `${path[1]}/save`);
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.send(JSON.stringify({ changes: changes }));
    changes = [];
    xhr.onload = () => {
      alert(xhr.response['is_saved']);
    };
  } else {
    alert("Нет изменений");
  }
};
