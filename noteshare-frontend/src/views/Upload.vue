<template>
  <v-container>
    <!-- Profile Header -->
    <v-row>
      <v-col>
        <v-card>
          <v-card-title>{{ user.name }}</v-card-title>
          <v-card-text>{{ user.bio }}</v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Profile Details -->
    <v-row>
      <v-col>
        <v-card>
          <v-card-title>Profile Details</v-card-title>
          <v-card-text>
            <p>Email: {{ user.email }}</p>
            <p>Location: {{ user.location }}</p>
            <!-- Add more details as needed -->
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Profile Actions -->
    <v-row>
      <v-col>
        <!-- Add any profile actions/buttons here -->
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      user: {
        name: 'John Doe',
        bio: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        email: 'john@example.com',
        location: 'City, Country'
        // Add more user details as needed
      }
    };
  }
};
</script>

<style scoped>
/* Add your scoped styles here */
</style>
