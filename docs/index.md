
# ICICLE Training Catalog

<button class="toggle-button" onclick="toggleView()">Toggle View</button>

<div id="cards-container" class="list-view">

<div class="card category1">
    <h3>Base ICICLE Tapis Software</h3>
    <p class="version">Version: 1.3.0</p>
    <p class="italic">Category: Category1</p>
    <p>Hosted, web-based API for managing data and executing software for research computing</p>
    <p><a href="https://tapis-project.github.io/tutorials/">Training Tutorials</a></p>
</div>

<div class="card category1">
    <h3>Tapis Pods Service API</h3>
    <p class="version">Version: 1.3.0</p>
    <p class="italic">Category: Category1</p>
    <p>New API providing web-accessible long-lived containers (pods) as-a-service via Kubernetes. Providing WAN-accessible Neo4J, Postgres, and custom-image HTTP pods with a simple API. More templates on the way.</p>
    <p><a href="https://tapis-project.github.io/tutorials/pods/intro/">Training Tutorials</a></p>
</div>

<div class="card category3">
    <h3>Tapis Pods Service API</h3>
    <p class="version">Version: 1.3.2</p>
    <p class="italic">Category: Category3</p>
    <p>New API providing web-accessible long-lived containers (pods) as-a-service via Kubernetes. Providing WAN-accessible Neo4J, Postgres, and custom-image HTTP pods with a simple API. More templates on the way.</p>
    <p><a href="https://tapis-project.github.io/tutorials/pods/intro/">Training Tutorials</a></p>
</div>

<div class="card category1">
    <h3>Tapis Pods Service API</h3>
    <p class="version">Version: 1.5.3</p>
    <p class="italic">Category: Category1</p>
    <p>New API providing web-accessible long-lived containers (pods) as-a-service via Kubernetes. Providing WAN-accessible Neo4J, Postgres, and custom-image HTTP pods with a simple API. More templates on the way.</p>
    <p><a href="https://tapis-project.github.io/tutorials/pods/intro/">Training Tutorials</a></p>
</div>

<div class="card category3">
    <h3>Tapis Pods Service API</h3>
    <p class="version">Version: 1.6.0</p>
    <p class="italic">Category: Category3</p>
    <p>New API providing web-accessible long-lived containers (pods) as-a-service via Kubernetes. Providing WAN-accessible Neo4J, Postgres, and custom-image HTTP pods with a simple API. More templates on the way.</p>
    <p><a href="https://tapis-project.github.io/tutorials/pods/intro/">Training Tutorials</a></p>
</div>

<div class="card category3">
    <h3>PPOD Core</h3>
    <p class="version">Version: 0.5.0</p>
    <p class="italic">Category: Category3</p>
    <p>A LinkML schema describing the core elements of PPOD (Person-Project-Organization-Dataset) information.</p>
    <p><a href="https://tapis-project.github.io/tutorials/pods/intro/">Training Tutorials</a></p>
</div>

</div>

<script>
function toggleView() {
  var container = document.getElementById('cards-container');
  if (container.classList.contains('list-view')) {
    container.classList.remove('list-view');
    container.classList.add('grid-view');
  } else {
    container.classList.remove('grid-view');
    container.classList.add('list-view');
  }
}
</script>
