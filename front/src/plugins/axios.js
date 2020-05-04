import axios from 'axios'

export default axios.create({
  baseURL: 'http://localhost:5000' // `${window.location.protocol}//${window.location.host}/${window.location.pathname}`
})
