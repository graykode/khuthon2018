<template>
    <div id="detailWrapper">
        <div id="map">
            <div class="content">
                <GmapMap
                   :center="{lat:37.2492188, lng:127.0721632}"
                    :zoom="16"
                    map-type-id="terrain"
                    style="width: 100%; height: 360px;"
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
            <div class="content">
                <div id="shop_detail">
                    <div id="shop_name">{{data.name}}</div>
                    <div id="shop_address"><span><i class="fas fa-map-marker-alt"></i></span>{{data.address}}</div>
                    <div id="shop_phone"><span><i class="fas fa-phone"></i></span>{{data.phone}}</div>
                    <div id="shop_category"><span><i class="fas fa-utensils"></i></span>{{data.category}}</div>
                    <div id="shop_price"><span><i class="fas fa-dollar-sign"></i></span>{{data.price}}</div>
                    <div id="shop_parking"><span><i class="fas fa-parking"></i></span>{{data.parking}}</div>
                    <div id="shop_time"><span><i class="fas fa-clock"></i></span>{{data.time}}</div>
                </div>
                <div id="star">
                    <i class="fas fa-star" v-bind={data} v-for="index in data.rate" :key="index"></i>
                    <div>이 점수는 머신러닝을 통해 산정된 결과입니다.</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import eventBus from '../commons/eventBus';
import {gmapApi} from 'vue2-google-maps';

export default {
    created(){
        eventBus.$on("wordClick", (data)=>{
            console.log("detail.vue",data);
        })
    },
    data(){
        return{
            data : {
                name : '수누리 감자탕 경희대점',
                address : '경기 수원시 영통구 덕영대로 1691',
                phone : '031-202-8441',
                category : '감자탕',
                price : '8,000원',
                parking : '주차가능',
                time : '24시간',
                rate : 3
            }
        }
    }
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
    box-shadow: 0 4px 8px 0 rgba(173, 75, 75, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
#map{
    height: 47.5%;
}
#evaluation{
    height: 47.5%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
#shop_detail{
    text-align: start
}
#shop_detail > *:not(#shop_name){
    margin-left:15px;
    margin-top:15px;
    color:#949494;
}
#shop_detail .fas{
    font-size: 20px;
    width: 40px;
}
#shop_name{
    text-align: center;
    font-weight: 700;
    font-size: 24px;
}
#star > :nth-last-child(1){
    margin-top: 10px;
    font-size: 12px;
    color: rgb(179, 179, 179);
}
.fa-star{
    margin-top: 15px;
    margin-left: 5px;
    font-size: 30px;
    color:#fffa00;
    text-shadow: 2px 2px 5px #000;
}
</style>
