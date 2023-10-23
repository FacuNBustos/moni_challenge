import User from "../interfaces/User";
import CommonServices from "./CommonServices";

class AuthServices extends CommonServices {
  public constructor() {
    super();
  }

  public async Login(credentials: User) {
    try {
      const response = await this.backend_axios.post("auth/login/", credentials);
      if (response.status != 200) {
        return false;
      }

      return response.data;
    } catch (_err) {
      return false;
    }
  }

  public async refresh(token: string) {
    try {
      const response = await this.backend_axios.post("auth/token/refresh/", {
        refresh: token,
      });
      if (response.status != 200) {
        return false;
      }

      return response.data;
    } catch (_err) {
      return false;
    }
  }

  public async verify(token: string) {
    try {
      const response = await this.backend_axios.post("auth/token/verify/", {
        token: token,
      });
      if (response.status != 200) {
        return false;
      }

      return true;
    } catch (_err) {
      return false;
    }
  }
}

export default new AuthServices();
