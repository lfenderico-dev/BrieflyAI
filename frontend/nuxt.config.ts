// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: ['@nuxtjs/tailwindcss', '@nuxt/icon', '@nuxt/image'],
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  app: {
    head:{
      title: 'NeuroClip',
      link: [
        {rel:'icon', type:'image/x-icon', href:'/media/favicon/NeuroClip.png'}
      ]
    }
  }
})