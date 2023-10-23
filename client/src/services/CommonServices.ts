import axios from "axios";

class CommonServices {
  protected backend_axios = axios.create({
    baseURL: "http://localhost:8000/api/v1/",
    headers: {
      "Content-Type": "application/json",
    },
  });
}

export default CommonServices;
