<template>
    <div class="flex flex-col gap-2 lg:gap-10 lg:flex-row-reverse items-center justify-center">
        <div class="wireframe lg:w-[50%] h-fit">
            <NuxtImg :src="media" class="size-[50%] mx-auto"></NuxtImg>
        </div>

        <div class="flex flex-col gap-2 lg:w-[50%]">
            <h2 class="header2 text-left">{{ title }}</h2>
            <p class="paragraph text-left">{{ description }}</p>
            <NuxtLink to="/explaination"  class="button flex justify-start w-fit text-lg">Try it now!</NuxtLink>
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
