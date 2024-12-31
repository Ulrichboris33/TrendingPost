<template>
  <div class="card">
    <img :src="topic.avatar_url" :alt="topic.name" />
    <div class="card-content">
      <h2 class="card-title" style="font-weight: bold;">{{ topic.name }}</h2>
      <p class="card-text">{{ topic.description || 'Pas de description disponible' }}</p>
      <span class="badge">{{ topic.stars }}</span>
      <a href="#" class="btn">{{ topic.language }}</a>  Dépôt créé le {{ topic.created_at }}
      
    </div>
  </div>
</template>

<script>
export default {
  props: {
    topic: {
      type: Object,
      required: true,
    },
  },
};
</script>

<style scoped>
.card {
  background: white;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin-bottom: 20px;
  display: flex;
  justify-content: space-between;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
}

.card img {
  width: 100px;
  height: auto;
  border-radius: 5px;
  transition: transform 0.3s ease;
}

.card img:hover {
  transform: scale(1.1);
}

.card-content {
  flex: 1;
  margin-left: 20px;
}

.card-title {
  font-size: 20px;
  font-weight: 500;
  margin: 0 0 10px 0;
  color: #333;
}

.card-text {
  font-size: 14px;
  color: #555;
  margin: 0 0 10px 0;
}

.badge {
  background-color: #f04f59;
  color: white;
  border-radius: 12px;
  padding: 6px 12px;
  font-size: 14px;
  font-weight: 700;
  margin-right: 10px;
}

.btn {
  background-color: #60c2b6;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 10px 20px;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
}

.btn:hover {
  background-color: #4aa69a;
}
</style>
