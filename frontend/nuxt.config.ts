// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: ['@nuxtjs/tailwindcss', '@nuxt/icon', '@nuxt/image', '@nuxtjs/supabase'],
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  supabase: {
    redirect: false
  },
  app: {
    head:{
      title: 'BrieflyAI',
      link: [
        {rel:'icon', type:'image/x-icon', href:'/favicon.png'}
      ]
    }
  }
})