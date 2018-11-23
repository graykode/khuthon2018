<template>
    <div id="detailWrapper">
        <div id="map">
            <div class="title">
                map
            </div>
            <div class="content">
                <GmapMap
                    :center="{lat:10, lng:10}"
                    :zoom="10"
                    map-type-id="terrain"
                    style="width: 100%; height: 100px;"
                        >
                        <!-- <GmapMarker
                            :key="index"
                            v-for="(m, index) in markers"
                            :position="m.position"
                            :clickable="true"
                            :draggable="true"
                            @click="center=m.position"
                        /> -->
                </GmapMap>
            </div>
        </div>
        <div id="evaluation">
            <div class="title">
                evaluation
            </div>
            <div class="content">
                
            </div>
        </div>
        <div id="comment">
            <div class="title">
                comment
            </div>
            <div class="content">
                    
            </div>
        </div>
    </div>
</template>

<script>
import {gmapApi} from 'vue2-google-maps'
export default {
}
</script>

<style>
#detailWrapper{
    height: 100%;

    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
#detailWrapper > *{
    background: #ffffff;
    margin-bottom: 15px;
}
#map{
    height: 30%;
}
#evaluation{
    height: 20%;
}
#comment{
    height: 40%;
}
.title{
    border: 1px solid red;
}
</style>
