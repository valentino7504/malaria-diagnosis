const imageInput = document.getElementById("imageInput");
const smear = document.getElementById("blood_smear");

function fillImage(event) {
  const [file] = imageInput.files;
  let fileName = "";
  if (file) {
    smear.classList.remove("hidden");
    smear.classList.add("block");
    document.getElementById("blood_smear").src = URL.createObjectURL(file);
    let imgName = document.querySelector(".img-name");
    fileName = event.target.value.split("\\").pop();
    imgName.textContent = fileName;
    imgName.classList.remove("hidden")
  }
}

function predict() {
  const img_file = document.getElementById("imageInput").files[0];
  const formData = new FormData();
  formData.append("smear_image", img_file);

  fetch("https://malaria-diagnosis.onrender.com/predict", {
    method: "POST",
    body: formData
  })
    .then(async response => {
      if (response.ok) {
        const data = await response.json();
        document.querySelector("span.para-value").textContent = data["parasitized"];
        document.querySelector("span.uninf-value").textContent = data["uninfected"];
        document.querySelector("span.diag-value").textContent = data["prediction"];
        if (data["prediction"] === "Uninfected") {
          document.querySelector("span.diag-value").style.color = "rgb(1, 78, 1)";
        } else {
          document.querySelector("span.diag-value").style.color = "red";
        }
      } else {
        console.log(response.status);
        console.log(response.statusText);
      }
    })
    .catch(error => console.error("Error: ", error));
}


imageInput.addEventListener("change", (event) => {
  fillImage(event);
  predict();
});
