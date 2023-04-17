const valid_var = ["5", "1", "2", "3", "4", "n"];

const inputs = document.querySelectorAll(".mark_input");
let add = [];
let removes = [];
const path = window.location.pathname.split("/");

inputs.forEach((input) => {
  input.addEventListener("input", (e) => {
    let valid = false;
    const get_value = e.target.value;
    const new_stud_id = input.parentElement.parentElement.id;
    const new_date = input.parentElement.id;

    const result_add = add.findIndex(
      ({ stud_id, date }) => stud_id === new_stud_id && date === new_date
    );

    const result_remove = add.findIndex(
      ({ stud_id, date }) => stud_id === new_stud_id && date === new_date
    );

    if (result_add > -1) {
      if (get_value == "") {
        add.splice(result_add, 1);
      }
    } else {
      valid_var.forEach((element) => {
        if (element == get_value) valid = true;
      });

      if (valid) {
        add.push({
          mark: get_value,
          stud_id: new_stud_id,
          date: new_date,
        });
      } else if (get_value == "") {
        removes.push({
          stud_id: new_stud_id,
          date: new_date,
        });
      } else if (!valid) e.target.value = "";
    }
  });
});

const save_button = document.getElementById("saveBtn");
var csrftoken = document.cookie
  .split("; ")
  .find((row) => row.startsWith("csrftoken="))
  ?.split("=")[1];

save_button.onclick = () => {
  if (add.length > 0 || removes.length > 0) {
    let xhr = new XMLHttpRequest();
    xhr.responseType = "json";
    xhr.open("POST", `${path[2]}/save`);
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.send(JSON.stringify({ add: add, removes: removes }));
    add = [];
    removes = [];
    xhr.onload = () => {
      alert(xhr.response["is_saved"]);
    };
  } else {
    alert("Нет изменений");
  }
};
