<style scoped>
  .container {
    display: flex;
    justify-content: center;
    padding: 2rem 1rem;
  }

  .form {
    background-color: #fff;
    display: block;
    padding: 2rem;
    width: 100%;
    max-width: 500px;
    border-radius: 0.75rem;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  }

  .form-title {
    font-size: 1.875rem;
    line-height: 2.25rem;
    font-weight: 600;
    text-align: center;
    color: #000;
    margin-bottom: 1.5rem;
  }

  .input-container {
    position: relative;
  }

  .input-container input, .form button {
    outline: none;
    border: 1px solid #e5e7eb;
    margin: 12px 0;
  }

  .input-container input {
    background-color: #fff;
    padding: 1.25rem;
    padding-right: 3rem;
    font-size: 1rem;
    line-height: 1.5rem;
    width: 100%;
    border-radius: 0.5rem;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    box-sizing: border-box;
  }

  .submit {
    display: block;
    padding: 1rem 1.5rem;
    background-color: #000000;
    color: #ffffff;
    font-size: 1rem;
    line-height: 1.5rem;
    font-weight: 500;
    width: 100%;
    border-radius: 0.5rem;
    text-transform: uppercase;
    cursor: pointer;
    transition: background-color 0.2s;
    margin-top: 1rem;
  }

  .submit:hover {
    background-color: #333333;
  }

  .toggle-link {
    color: #6B7280;
    font-size: 0.875rem;
    line-height: 1.25rem;
    text-align: center;
    margin-top: 1rem;
  }

  .toggle-link button {
    background: none;
    border: none;
    color: #4F46E5;
    text-decoration: underline;
    cursor: pointer;
    font-size: 0.875rem;
    padding: 0;
    font-weight: 500;
  }

  .toggle-link button:hover {
    color: #4338CA;
  }

  /* Large screens - even bigger */
  @media (min-width: 1024px) {
    .form {
      max-width: 600px;
      padding: 3rem;
      border-radius: 1rem;
    }

    .form-title {
      font-size: 2.25rem;
      line-height: 2.5rem;
      margin-bottom: 2rem;
    }

    .input-container input {
      padding: 1.5rem;
      font-size: 1.125rem;
    }

    .submit {
      padding: 1.25rem 2rem;
      font-size: 1.125rem;
      margin-top: 1.5rem;
    }
  }

  /* Tablet and medium screens */
  @media (min-width: 768px) and (max-width: 1023px) {
    .form {
      max-width: 550px;
      padding: 2.5rem;
    }

    .form-title {
      font-size: 2rem;
      margin-bottom: 1.75rem;
    }

    .input-container input {
      padding: 1.375rem;
      font-size: 1.0625rem;
    }

    .submit {
      padding: 1.125rem 1.75rem;
      font-size: 1.0625rem;
    }
  }

  /* Mobile responsiveness */
  @media (max-width: 767px) {
    .form {
      padding: 1.5rem 1rem;
      margin: 0 0.5rem;
      max-width: 400px;
    }

    .form-title {
      font-size: 1.5rem;
      margin-bottom: 1rem;
    }

    .input-container input {
      padding: 1rem;
      font-size: 1rem;
    }

    .submit {
      padding: 0.875rem 1rem;
      font-size: 1rem;
    }
  }

  /* Extra small devices */
  @media (max-width: 375px) {
    .form {
      padding: 1rem 0.75rem;
      margin: 0 0.25rem;
      max-width: 350px;
    }

    .form-title {
      font-size: 1.25rem;
    }

    .input-container input {
      padding: 0.875rem;
      font-size: 0.9375rem;
    }
  }
</style>

<template>
    <div class="container">
        <form class="form" @submit.prevent="() => (isSignUp ? signUp() : login())">
            <p class="form-title">{{ isSignUp ? 'Create your account' : 'Sign in to your account' }}</p>
            <div class="input-container">
                <input type="email" placeholder="Enter email" v-model="email" required>
                <span>
                </span>
            </div>
            <div class="input-container">
                <input type="password" placeholder="Enter password" v-model="password" required>
            </div>
            <button type="submit" class="submit">{{ isSignUp ? 'Sign Up' : 'Sign In' }}</button>
            <p class="toggle-link">
                {{ isSignUp ? 'Already have an account?' : "Don't have an account?" }}
                <button type="button" @click="isSignUp = !isSignUp">
                    {{ isSignUp ? 'Sign In' : 'Sign Up' }}
                </button>
            </p>
        </form>
    </div>
</template>


<script setup lang="ts">
const email = ref<string>('')
const password = ref<string>('')
const isSignUp = ref<boolean>(false)

const client = useSupabaseClient()
const user = useSupabaseUser()

const signUp = async () => {
  const { data, error } = await client.auth.signUp({
    email: email.value,
    password: password.value
  })
  
  if (error) {
    console.error('Sign up error:', error.message)
    alert('Sign up failed: ' + error.message)
  } else {
    console.log('Sign up successful')
    alert('Sign up successful! Please check your email to confirm your account.')
  }
}

const login = async () => {
  const { data, error } = await client.auth.signInWithPassword({
    email: email.value,
    password: password.value
  })
  
  if (error) {
    console.error('Login error:', error.message)
    alert('Login failed: ' + error.message)
  } else {
    console.log('Login successful')
    navigateTo('/')
  }
}
</script>
