<template>
  <div>
    <gmap-map
        :center="center"
        :zoom="16"
        style="width: 100%; height: 345px;"
    >
    <gmap-marker
        :key="index"
        v-for="(m, index) in markers"
        :position="m.position"
        @click="center=m.position"
    ></gmap-marker>
    </gmap-map>
  </div>
</template>

<script>
import eventBus from '../commons/eventBus';
import axios from 'axios';
import confidential from '../confidential/confidential.json'

export default {
    name: "GoogleMap",
    created(){
        eventBus.$on('setLocation',(data)=>{
            this.markers = [];
            this.geocode(data);
        })
    },
    data() {
        return {
            // default to Montreal to keep it simple
            // change this to whatever makes sense
            center: { lat:37.2492188, lng:127.0721632 },
            markers: [],
            places: [],
            currentPlace: null
        };
    },

  mounted() {
    this.geolocate();
  },

  methods: {
    // receives a place object via the autocomplete component
    geocode(location){
        axios.get('https://maps.googleapis.com/maps/api/geocode/json',{
            params:{
                address:location,
                key: confidential.google_geocoding_api
            }
        })
        .then((response)=>{
            this.addMarker(response.data.results[0].geometry);
        })
        .catch((error)=>{
            console.log(error);
        });
    },
    addMarker(geometry) {
        if(geometry) {
            const marker = {
                lat: geometry.location.lat,
                lng: geometry.location.lng
            };
            this.markers.push({ position: marker });
            //this.places.push(this.currentPlace);
            this.center = marker;
            this.currentPlace = null;
        }
    },
    geolocate: function() {
      navigator.geolocation.getCurrentPosition(position => {
        this.center = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
      });
    }
  }
};
</script>