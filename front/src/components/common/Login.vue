<template>
  <el-row>
    <el-col :span="10">
      <el-carousel :interval="4000" type="card">
        <el-carousel-item v-for="item in 3" :key="item">
          <h3> </h3>
        </el-carousel-item>
      </el-carousel>
    </el-col>
    <el-col :span="8" :offset="3">
      <el-form :rules='loginRule' :model='login' label-position="left" class="login_form">
      <h3 class="title">系统登录</h3>
        <el-form-item prop="username">
          <el-input type='text' v-model.trim='login.username' placeholder='账号'></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input type='password' v-model.trim='login.password' placeholder='密码'></el-input>
        </el-form-item>
        <el-checkbox v-model="checked" checked>记住密码</el-checkbox>
        <el-form-item >
          <el-button type='primary' @click='toLogin' style="width:100%" :loading='loading'>登录</el-button>
        </el-form-item>
      </el-form>
    </el-col>
  </el-row>
</template>

<script>
  export default{
    data(){
      return{
        checked:true,
        loading:false,
        login:{username:'',password:''},
        loginRule:{
          username:[{required:true,message:'请输入账号',trigger:'blur'}],
          password:[{required:true,message:'请输入密码',trigger:'blur'}]
        }
      }
    },
    methods:{
      toLogin(){
        if(1==1){
          sessionStorage.setItem('username',JSON.stringify('admin'))
          sessionStorage.setItem('usertoken',JSON.stringify('admin'))
          this.$router.push('/me')
        }else{
          this.$message.error({message:'error',center:true})
        }
      }
    }
  }
</script>
<style>
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
  .login_form{
    border-radius: 5px;
    padding: 35px;
    box-shadow: 0 0 25px #cac6c6;
  }
</style>