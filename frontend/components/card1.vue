<template>
    <div class="flex flex-col gap-2">
        <div class="wireframe">
            <media :src="media" class="object-contain"></media>
        </div>

        <div class="flex flex-col gap-2">
            <h2 class="header2 text-left">{{ title }}</h2>
            <p class="paragraph text-left">{{ description }}</p>
            <NuxtLink to="/app"  class="button flex justify-start w-fit text-lg">Try it now!</NuxtLink>
        </div>
    </div>
</template>

<script setup lang="ts">
defineProps<{
    media: string
    title: string
    description?: string 
}>()
</script>
