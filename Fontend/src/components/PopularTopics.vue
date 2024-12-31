<template>
  <div class="container">
    <h1 class="title">Trending Repos</h1>
    <div class="toolbar">
      <!-- Barre de recherche -->
      <div class="search-bar">
        <input type="text" v-model="searchQuery" placeholder="Rechercher un dépôt..." @input="filterBySearch" />
      </div>
      <!-- Dropdown for languages -->
      <div class="language-selector">
        <label for="language"> Language:</label>
        <select v-model="selectedLanguage" @change="filterByLanguage">
          <option value="">All</option>
          <option v-for="language in languages" :key="language.id" :value="language.language">
            {{ language.language }}
          </option>
        </select>
      </div>
    </div>
    <!-- Affichage de l'indicateur de chargement -->
    <div v-if="loading" class="loading-spinner">
      <span>Chargement...</span>
    </div>
    <!-- Repositories list -->
    <div v-for="topic in paginatedTopics" :key="topic.id">
      <TopicCard :topic="topic" />
    </div>

    <!-- Pagination -->
    <div class="pagination">
      <a href="#" @click.prevent="prevPage" :class="{ disabled: currentPage === 1 }">Prev</a>
      <a v-for="page in totalPages" :key="page" href="#" @click.prevent="goToPage(page)"
        :class="{ active: currentPage === page }">
        {{ page }}
      </a>
      <a href="#" @click.prevent="nextPage" :class="{ disabled: currentPage === totalPages }">Next</a>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import TopicCard from "./TopicCard.vue";

export default {
  components: {
    TopicCard,
  },
  data() {
    return {
      topics: [],  // Liste des topics
      languages: [],  // Liste des langages
      selectedLanguage: '',  // Langage sélectionné
      searchQuery: '',  // Texte de recherche
      currentPage: 1,
      itemsPerPage: 10,
      loading: false,  // Indicateur de chargement
      error: null,  // Message d'erreur
    };
  },
  created() {
    this.fetchTopics();  // Appel de la méthode pour récupérer les topics au chargement du composant
    this.fetchLanguages();  // Récupérer les langages disponibles
  },
  computed: {
    totalPages() {
      return Math.ceil(this.filteredTopics.length / this.itemsPerPage);
    },
    paginatedTopics() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      return this.filteredTopics.slice(start, start + this.itemsPerPage);
    },
    filteredTopics() {
      let filtered = this.topics;

      // Filtrage par langage
      if (this.selectedLanguage) {
        filtered = filtered.filter(topic => topic.language === this.selectedLanguage);
      }

      // Filtrage par recherche
      if (this.searchQuery) {
        const query = this.searchQuery.toLowerCase();
        filtered = filtered.filter(topic =>
          topic.name.toLowerCase().includes(query) ||
          (topic.description && topic.description.toLowerCase().includes(query))
        );
      }

      return filtered;
    },
  },
  methods: {
    // Récupérer les topics depuis l'API
    async fetchTopics() {
      this.loading = true;
      this.error = null;
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/repositories/');
        console.log(response.data);
        this.topics = response.data;
      } catch (err) {
        this.error = "Impossible de récupérer les topics.";
        console.error(err);
      } finally {
        this.loading = false;
      }
    },

    // Récupérer les langages depuis l'API
    async fetchLanguages() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/languages/');
        console.log(response.data);
        this.languages = response.data;
      } catch (err) {
        console.error("Error fetching languages", err);
      }
    },

    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
    goToPage(page) {
      this.currentPage = page;
    },
    filterByLanguage() {
      // Filtering logic is handled by computed property `filteredTopics`
      this.currentPage = 1; // Reset to first page after filtering
    },
    filterBySearch() {
      // Le filtrage est géré par la propriété calculée `filteredTopics`
      this.currentPage = 1; // Réinitialiser à la première page après filtrage
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
}

.toolbar {
  display: flex;
  justify-content: space-between;
  /* Positionne les éléments à l'opposé */
  align-items: center;
  /* Aligne verticalement les éléments */
  margin-bottom: 20px;
  /* Espacement en dessous */
}

.title {
  text-align: center;
  font-size: 28px;
  font-weight: 500;
  margin-bottom: 30px;
  color: #fff;
  /* Couleur du texte */
  background-color: #60c2b6;
  /* Couleur de fond */
  padding: 15px 20px;
  /* Rembourrage pour un effet entête */
  border-radius: 8px;
  /* Coins arrondis */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  /* Ombre pour donner du relief */
}

/* Indicateur de chargement */
.loading-spinner {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
  font-size: 18px;
  color: #60c2b6;
}

.loading-spinner span {
  animation: loading 1.5s infinite;
}

@keyframes loading {
  0% {
    transform: translateX(-10px);
  }

  50% {
    transform: translateX(10px);
  }

  100% {
    transform: translateX(-10px);
  }
}


.language-selector {
  margin-bottom: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.language-selector select {
  padding: 8px;
  font-size: 14px;
  border-radius: 5px;
  border: 1px solid #ddd;
}

/* Barre de recherche */
.search-bar input {
  padding: 10px;
  border-radius: 25px;
  border: 1px solid #ddd;
  font-size: 16px;
  width: 300px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: border 0.3s;
  margin-bottom: 20px;
}

.search-bar input:focus {
  border: 1px solid #60c2b6;
  outline: none;
  box-shadow: 0 0 10px rgba(96, 194, 182, 0.5);
}

.filter-dropdown select:focus {
  box-shadow: 0 0 10px rgba(96, 194, 182, 0.5);
  outline: none;
}

.pagination {
  display: flex;
  justify-content: center;
  margin-top: 30px;
}

.pagination a {
  margin: 0 5px;
  text-decoration: none;
  color: #60c2b6;
  font-size: 14px;
  font-weight: 500;
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 5px;
  transition: background-color 0.2s, color 0.2s;
}

.pagination a.active {
  background-color: #60c2b6;
  color: white;
}

.pagination a:hover {
  background-color: #4aa69a;
  color: white;
}

.pagination a.disabled {
  pointer-events: none;
  opacity: 0.5;
}
</style>
