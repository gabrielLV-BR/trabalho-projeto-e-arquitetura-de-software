// STATE (Observer simples)
const state = {
  year: 2022,
  category: "publico",
  modality: "presencial",
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

// API CALLS
async function fetchTotal() {
  const res = await fetch(`/alunos/total/${state.year}`);
  return res.json();
}

async function fetchCourses() {
  const res = await fetch(`/cursos/ranking/${state.year}/${state.category}/${state.modality}`);
  return res.json();
}

async function fetchInstitutions() {
  const res = await fetch(`/instituicoes/ranking/${state.year}/${state.category}/${state.modality}`);
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
  } catch {
    alert("Erro ao carregar cursos");
  }
}

async function renderInstitutions() {
  const tbody = document.querySelector("#institutionsTable tbody");
  tbody.innerHTML = "";

  try {
    const data = await fetchInstitutions();

    data.forEach(item => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${item.position}</td>
        <td>${item.institution.name}</td>
        <td>${item.totalStudents}</td>
      `;
      tbody.appendChild(tr);
    });
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