<template>
  <div class="register-container">
    <div class="register-box">
      <h1 style="font-size: 24px">欢迎注册实验室预约系统</h1>

      <el-form :model="form" label-width="auto" style="max-width: 600px">
        <el-form-item label="Activity name">
          <el-input
            size="large"
            v-model="form.username"
            placeholder="请输入账号"
            prefix-icon="User"
          />
        </el-form-item>
        <el-form-item label="Password">
          <el-input
            size="large"
            v-model="form.password"
            placeholder="请输入密码"
            :prefix-icon="Lock"
            type="password"
            show-password
          />
        </el-form-item>
        <el-form-item label="confirmPassword">
          <el-input
            size="large"
            v-model="form.comfirmPassword"
            placeholder="请确认密码"
            :prefix-icon="Lock"
            type="password"
            show-password
          />
        </el-form-item>

        <div>
          <el-button type="primary" size="large" style="width: 100%"> 注 册 </el-button>
          <div style="margin-top: 20px; text-align: right">
            已有账号？请 <a style="color: var(--el-color-primary)" href="/login">登录</a>
          </div>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue'
import { User, Lock } from '@element-plus/icons-vue'
import { ElFormItem } from 'element-plus'
const form = reactive({
  username: '',
  password: '',
  comfirmPassword: ''
})
</script>

<style>
.register-container {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
.register-box {
  width: 380px;
  border-radius: 8px;
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.1);
  text-align: center;
  padding: 30px;
  background-color: #fff;
}
</style>
