// STATE (Observer simples)
const state = {
  year: 2022,
  category: "publico",
  modality: "presencial",
  coursePage: 1,
  institutionPage: 1,
  listeners: [],

  subscribe(fn) {
    this.listeners.push(fn);
  },

  notify() {
    this.listeners.forEach(fn => fn());
  }
};

// Atualiza estado
document.getElementById("year").addEventListener("change", (e) => {
  state.year = e.target.value;
  state.notify();
});

document.getElementById("category").addEventListener("change", (e) => {
  state.category = e.target.value;
  state.notify();
});

document.getElementById("modality").addEventListener("change", (e) => {
  state.modality = e.target.value;
  state.notify();
});

document.getElementById("institutionPagePrevious").addEventListener("click", (e) => {
  if (state.institutionPage > 1) {
    state.institutionPage -= 1;
    state.notify();
  }
});

document.getElementById("institutionPageNext").addEventListener("click", (e) => {
  state.institutionPage += 1;
  state.notify();
});


document.getElementById("coursePagePrevious").addEventListener("click", (e) => {
  if (state.coursePage > 1) {
    state.coursePage -= 1;
    state.notify();
  }
});

document.getElementById("coursePageNext").addEventListener("click", (e) => {
  state.coursePage += 1;
  state.notify();
});


// API CALLS
async function fetchTotal() {
  const res = await fetch(`/alunos/total/${state.year}`);
  return res.json();
}

async function fetchCourses() {
  const res = await fetch(`/cursos/ranking/${state.year}/${state.category}/${state.modality}?page=${state.coursePage}`);
  return res.json();
}

async function fetchInstitutions() {
  const res = await fetch(`/instituicoes/ranking/${state.year}/${state.category}/${state.modality}?page=${state.institutionPage}`);
  return res.json();
}

// RENDER
async function renderTotals() {
  try {
    const data = await fetchTotal();
    document.getElementById("totalPresential").textContent = data.totalStudentsPresential;
    document.getElementById("totalEAD").textContent = data.totalStudentsEAD;
    document.getElementById("totalAll").textContent = data.totalStudents;
  } catch {
    alert("Erro ao carregar totais");
  }
}

async function renderCourses() {
  const tbody = document.querySelector("#coursesTable tbody");
  const page = document.querySelector("#coursePage")
  tbody.innerHTML = "";

  try {
    const data = await fetchCourses();

    data.forEach(item => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${item.position}</td>
        <td>${item.course.name}</td>
        <td>${item.totalRegistrations}</td>
      `;
      tbody.appendChild(tr);
    });

    page.innerHTML = `${state.coursePage}`
  } catch {
    alert("Erro ao carregar cursos");
  }
}

async function renderInstitutions() {
  const tbody = document.querySelector("#institutionsTable tbody");
  const page = document.querySelector("#institutionPage")
  tbody.innerHTML = "";

  try {
    const data = await fetchInstitutions();

    data.forEach(item => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${item.position}</td>
        <td>${item.institution.ies}</td>
        <td>${item.totalStudents}</td>
      `;
      tbody.appendChild(tr);
    });

    page.innerHTML = `${state.institutionPage}`
  } catch {
    alert("Erro ao carregar instituições");
  }
}

// Observer funcionando
state.subscribe(renderTotals);
state.subscribe(renderCourses);
state.subscribe(renderInstitutions);

// Inicialização
state.notify();