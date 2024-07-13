<!-- src/views/LandingPage.vue -->
<template>
  <v-app>
    <!--the Navbar-->
    <v-app-bar app color="E1C2BB" text-white dark>
      <v-icon color="yellow" left class="mr-2">fas fa-signature</v-icon>NOTESHARE
      <v-spacer></v-spacer>
      <v-btn text>
        <router-link to="/profile" class="white--text">Profile</router-link>
      </v-btn>
      <v-btn text>
        <router-link to="/about" class="white--text">About Us</router-link>
      </v-btn>
      <v-btn text>
        <router-link to="/signup" class="white--text">Sign Up</router-link>
      </v-btn>
      <v-btn text>
        <router-link to="/login" class="white--text">Login</router-link>
      </v-btn>
    </v-app-bar>
      <v-container>
        <v-row align="center">
          <v-col cols="auto">
          
            
          </v-col>
          <v-col class="d-none d-lg-flex">
            <v-btn text href="#services">Services</v-btn>
            <v-spacer></v-spacer>
            <v-btn text href="#features">Features</v-btn>
            <v-menu offset-y>
              <template v-slot:activator="{ on, attrs }">
              </template>
              <v-list>
                <v-list-item link>
                  <v-list-item-title>Article Details</v-list-item-title>
                </v-list-item>
                <v-divider></v-divider>
                <v-list-item link>
                  <v-list-item-title>Terms Conditions</v-list-item-title>
                </v-list-item>
                <v-divider></v-divider>
                <v-list-item link>
                  <v-list-item-title>Privacy Policy</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </v-col>
          <v-col class="d-flex justify-end">
            <v-btn outlined href="#contact">Get quote</v-btn>
          </v-col>
        </v-row>
      </v-container>

    <v-main>
      <header id="header" class="header">
        <v-container class="custom-container">
          <v-row>
            <v-col cols="12" lg="6">
              <div class="text-container">
                <h1 class="display-1">Empower Learning Together</h1>
                <p class="subtitle-1">NoteShare is a collaborative platform designed to facilitate seamless sharing of academic notes among students across universities, 
                  colleges, and high schools. It empowers learners to enhance their educational journey by accessing a diverse array of study materials contributed by peers.
                   Whether preparing for exams, researching topics, or exploring new subjects,
                   NoteShare fosters a supportive community where knowledge is shared, connections are forged, and learning becomes a collective endeavor.</p>
                <v-btn large class="custom-gradient" color="primary" href="#services">Available Subjects</v-btn>
              </div>
            </v-col>
            <v-col cols="12" lg="6">
              <v-img src="/assets/images/virtualLibrary.jpg" alt="alternative"></v-img>
            </v-col>
          </v-row>
        </v-container>
      </header>
      <v-container>
        <v-row>
          <v-col cols="12" lg="6">
          <v-img src="/assets/images/virtualLibrary.jpg" alt="alternative"></v-img>
        </v-col>
            <v-col cols="12" lg="6">
              <div class="text-container">
                <h1 class="display-1">Unlock Your Academic Potential</h1>
                <p class="subtitle-1">"Dive into a pool of knowledge shared by fellow students. NoteShare is your gateway to better grades and a richer educational experience."
                  Join a community of learners. Share notes, gain insights, and achieve your academic goals with the help of NoteShare.
                </p>
                <v-btn large class="custom-gradient" color="primary" href="#services">Available Subjects</v-btn>
              </div>
            </v-col>
            <v-col cols="12" lg="6">
              <v-img src="/assets/images/virtualLibrary.jpg" alt="alternative"></v-img>
            </v-col>
          </v-row>
        </v-container>

      <v-container class="custom-container py-10">
        <v-row>
          <v-col class="text-center">
            <v-btn color="black" class="cusstom-gradient">University</v-btn>
            <v-btn color="black" class="ma-2">College</v-btn>
            <v-btn color="black" class="ma-2">High School</v-btn>
          </v-col>
        </v-row>
        <v-row>
          <v-col class="text-center">
            <h1 class="font-weight-bold">Sharing notes and knowledge</h1>
            <p>Find top related study notes from students sharing the same course</p>
          </v-col>
        </v-row>
        <v-row>
          <v-col class="text-center">
            <v-text-field
              class="mt-8"
              label="Search for documents"
              outlined
              dense
            ></v-text-field>
            <p>Only the best</p>
          </v-col>
        </v-row>
      </v-container>

      <v-container id="services" class="custom-container">
        <v-row>
          <v-col>
            <h2>Explore our Offers</h2>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="4" v-for="service in services" :key="service.title">
            <v-card>
              <v-card-title class="justify-center">{{ service.title }}</v-card-title>
              <v-card-subtitle class="text-center">{{ service.subtitle }}</v-card-subtitle>
              <v-card-actions>
                <v-btn text href="#">{{ service.linkText }} <v-icon right>mdi-arrow-right</v-icon></v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>

      <v-container id="details" class="gradient-container py-19">
        <v-row>
          <v-col cols="12" lg="6">
            <v-img src="assets/images/details-1.png" alt="alternative"></v-img>
          </v-col>
          <v-col cols="12" lg="6">
            <div class="text-container">
              <h2>Share Learn Succeed</h2>
              <p class="bold">Discover the power of peer collaboration, NOTESHARE connects you with the notes you need to excel</p>
              <p>"With NoteShare, you're just a note away from excellence. Connect, collaborate, and succeed with the shared wisdom of your peers."
                "Join a community of learners. Share notes, gain insights, and achieve your academic goals with the help of NoteShare."

              </p>
              <v-btn color="primary" href="#contact">Get Study Plan</v-btn>
            </div>
          </v-col>
        </v-row>
      </v-container>

      <v-container id="features" class="custom-container py-19">
        <v-row>
          <v-col cols="12">
            <h2 class="text-center">Available Subjects</h2>
            <p class="text-center">Explore a variety of Subjects for different educational Levels</p>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="4">
            <v-card class="subject-card gradient-container">
              <v-card-title class="text-center">University<</v-card-title>
              <v-card-subtitle class="text-center, blue">Advanced subjects for university students.</v-card-subtitle>
              <v-card-text >
                <ul class="custom-gradient">
                  <li>Mathematics</li>
                  <li>Physics</li>
                  <li>Computer Science</li>
                  <li>Engineering</li>
                </ul>
              </v-card-text>
            </v-card>
            </v-col>
            <!--College-->
            <v-col cols="12" md="4">
            <v-card class="subject-card gradient-container">
              <v-card-title class="text-center">College</v-card-title>
              <v-card-subtitle class="text-center">Core subjects for college students.</v-card-subtitle>
              <v-card-text>
                <ul class="custom-gradient">
                  <li>Biology</li>
                  <li>Chemistry</li>
                  <li>Business Studies</li>
                  <li>Psychology</li>
                  <!-- Add more subjects as needed -->
                </ul>
              </v-card-text>
            </v-card>
          </v-col>
          <!-- High School Subjects -->
          <v-col cols="12" md="4">
            <v-card class="subject-card gradient-container">
              <v-card-title class="text-center">High School</v-card-title>
              <v-card-subtitle class="text-center">Fundamental subjects for high school students.</v-card-subtitle>
              <v-card-text>
                <ul class="custom-gradient">
                  <li>History</li>
                  <li>Geography</li>
                  <li>Literature</li>
                  <li>Biology</li>
                  <!-- Add more subjects as needed -->
                </ul>
              </v-card-text>
            </v-card>
          </v-col>
          
           <v-col cols="12">
            <v-accordion v-model="accordion">
              <v-accordion-item v-for="feature in features" :key="feature.title" :value="feature.value">
                <template v-slot:header>
                  <v-icon left>{{ feature.icon }}</v-icon>
                  {{ feature.title }}
                </template>
                <div>{{ feature.description }}</div>
              </v-accordion-item>
            </v-accordion>
           </v-col>
          
          <v-col cols="12" lg="7">
            <v-img src="assets/images/features-dashboard.png" alt="alternative"></v-img>
          </v-col>
        </v-row>
      </v-container>

      <v-container class="gradient-container py-10">
        <v-row>
          <v-col cols="12">
            <h2 class="text-center">Students testimonials</h2>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="4" v-for="testimonial in testimonials" :key="testimonial.author">
            <v-card class="testimonial-card" color="white">
              <v-card-title class="testimonial-text">
                <v-icon left class=""quote-icon>mdi-format-quote-close</v-icon>
                <span>{{ testimonial.text }}</span>
                <p class="occupation-text">College Students</p>
              </v-card-title>
              <v-card-subtitle class="text-center author-text">{{ testimonial.author }}</v-card-subtitle>
              <v-card-subtitle class="text-center occupation-text">{{ testimonial.occupation }}</v-card-subtitle>
            </v-card>
          </v-col>
        </v-row>
      </v-container>

      <v-container class="custom-container py-10">
        <v-row>
          <v-col cols="12">
            <h4 class="text-center trusted-title">Trusted by over <span class="blue--text">5000</span> students worldwide</h4>
            <v-divider class="my-4"></v-divider>
          </v-col>
        </v-row>
        <v-row justify="center">
          <v-col cols="12" md="2" v-for="logo in logos" :key="logo">
            <v-img :src="logo" alt="alternative"></v-img>
          </v-col>
        </v-row>
      </v-container>

      <v-container id="contact" class="gradient-container py-10">
        <v-row>
          <v-col cols="12" lg="6">
            <div class="text-container">
              <h2>Request a personalized Study Plan quote</h2>
              <p>At NoteShare we understand that every student's learning journey is unique.
                whether you need tailored study plan, one-on-one tutoring, or access to premium study materials.
                We are here to help
              </p>
              <ul>
                <li v-for="(item, index) in contactList" :key="index">
                  <v-icon left>mdi-square</v-icon>
                  {{ item }}
                </li>
              </ul>
            </div>
          </v-col>
          <v-col cols="12" lg="6">
            <v-form>
              <v-text-field label="Name" required></v-text-field>
              <v-text-field label="Email" required></v-text-field>
              <v-text-field label="Level of Education" required></v-text-field>
              <v-text-field label="Your plan" required></v-text-field>
              <v-btn color="primary" type="submit">Submit</v-btn>
            </v-form>
          </v-col>
        </v-row>
      </v-container>

      <!--Bottom bar-->
      <v-footer class=" custom-container py-20">
        <v-container>
          <v-row>
            <v-col cols="12" class="text-center">
              <h4>Keep up with recent updates.follow us</h4>
              <v-btn icon href="#your-link"><v-icon>mdi-facebook</v-icon></v-btn>
              <v-btn icon href="#your-link"><v-icon>mdi-twitter</v-icon></v-btn>
              <v-btn icon href="#your-link"><v-icon>mdi-pinterest</v-icon></v-btn>
              <v-btn icon href="#your-link"><v-icon>mdi-instagram</v-icon></v-btn>
              <v-btn icon href="#your-link"><v-icon>mdi-youtube</v-icon></v-btn>
            </v-col>
          </v-row>
        </v-container>
      </v-footer>

      <!--Footer with links-->
      <v-footer class="gradient-container">
        <v-container>
          <v-row>
            <v-col cols="12" lg="6" class="text-center">
              <v-list dense>
                <v-list-item link>
                  <v-list-item-title class="custom-gradien">Home</v-list-item-title>
                  </v-list-item>
                  <v-list-item link>
                    <v-list-item-title>About</v-list-item-title>
                  </v-list-item>
                  <v-list-item link>
                    <v-list-item-title>Contact</v-list-item-title>
                  </v-list-item>
                  </v-list>
                  </v-col>
                  <v-col cols="12" ig ="6" class="text-center">
                    <p>Subscribe to our news letter for the latest updates</p>
                    <v-form>
                      <v-text-field label="Email" type="email" solo></v-text-field>
                      <v-btn color="primary">Subscribe</v-btn>
                    </v-form>
                    </v-col>
          </v-row>
          </v-container>
          </v-footer>
    </v-main>
          </v-app>
  </template>

<script>
export default {
  name: 'LandingPage',
  data(){
    return {
      testimonials: [
        {
          text: "NoteShare has revolutionized the way I study. Accessing notes from peers has helped me understand complex topics better.",
          author: "Jane Doe",
          occupation: "University Student"
        },
        {
          text: "As a college student, NoteShare has become my go-to resource for finding reliable study materials quickly.",
          author: "John Smith",
          occupation: "College Student"
        },
        {
          text: "As a college student, NoteShare has become my go-to resource for finding reliable study materials quickly.",
          author: "John Smith",
          occupation: "College Student"
        }

      ],
      reviews: [
        {
          text: "This platform is amazing! It has helped me improve my grades significantly.",
          author: "Alex Brown",
          occupation: "University Student"
        },
        {
          text: "I love how easy it is to find notes for my subjects. Highly recommend!",
          author: "Sara White",
          occupation: "College Student"
        },
        {
          text: "The best study tool I've ever used. A must-have for all students.",
          author: "Michael Green",
          occupation: "High School Student"
        }
      ],
      logos: [
        'logo 1.jpg',
        'logo 2.jpg',
        'logo 3.jpg',
        'logo 4.jpg',
      ],
      features: [
        {
          icon: 'mdi-book-open-page-variant',
          title: 'Wide Range of Subjects',
          description: 'Access a comprehensive collection of notes and study materials for various subjects across different levels.',
          value: 'subjects'
        },
        {
          icon: 'mdi-account-group',
          title: 'Collaborative Learning',
          description: 'Connect with peers, share knowledge, and enhance your learning experience through collaboration.',
          value: 'collaboration'
        },
        {
          icon: 'mdi-check-circle-outline',
          title: 'Quality Resources',
          description: 'Find well-organized, high-quality study materials contributed by students and educators.',
          value: 'quality'
        }
      ]
    };
  },
  methods: {
    goToProfile() {
      this.$router.push({ name: 'Profile' });
    },
    goToAboutUs() {
      this.$router.push({ name: 'AboutUs' });
    }
  }
};
</script>

<style scoped>
.custom-container {
  background-color:#055e64;
  padding: 20px;
}
.custom-footer {
  background-color: linear-gradient( to right, #055e64, rgb(38, 70, 10));
  padding: 20px;
}
.gradient-container {
  background: linear-gradient(to right, #8ecece, rgb(37, 69, 78));
  padding: 20px;
}
.bg-gray {
  background-color: #584e4e;
}

.text-center {
  text-align: center;
}

.py-10 {
  padding-top: 10px;
  padding-bottom: 10px
}

.py-5 {
  padding-top: 5px;
  padding-bottom: 5px;
}
.v-application {
  background-color: #055e64;
}
.v-btn .router-link-active {
  text-decoration: none;
  color: inherit;
}
.custom-gradient {
  --gradient-color: linear-gradient(to right, rgba(0,0,0,0.8), rgba(0,0,0,0.4));
}

/* Apply the gradient to the button */
.v-btn.custom-gradient {
  background-color: black;
  background-image: linear-gradient(to right, rgba(0,0,0,0.8), rgba(0,0,0,0.4));
  background: var(--gradient-color);
  color: white; /* Text color */
  border-color: transparent; /* Optional: Remove border color */
}

.testimonials-title {
  font-family: 'Roboto', sans-serif;
  font-size: 2.5rem;
  color: #ffffff;
  margin-bottom: 20px;
}

.testimonial-card {
  background-color: #ffffff;
  border-radius: 10px;
  padding: 20px;
  margin-bottom: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.testimonial-text {
  font-family: 'Open Sans', sans-serif;
  font-size: 1rem;
  color: #333333;
}

.quote-icon {
  color: #ff7e5f;
}

.author-text {
  font-family: 'Roboto', sans-serif;
  font-size: 1.2rem;
  color: #333333;
  margin-top: 10px;
}

.occupation-text {
  font-family: 'Open Sans', sans-serif;
  font-size: 1rem;
  color: #777777;
}

.trusted-title {
  font-family: 'Roboto', sans-serif;
  font-size: 1.5rem;
  color: #333333;
}

.logo-image {
  width: 100%;
  height: auto;
  max-width: 150px;
  margin: 0 auto;
}

.blue--text {
  color: #3b82f6;
}
</style>
