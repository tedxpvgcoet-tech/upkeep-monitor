import axios from 'axios';

const URL = "https://www.backend.tedxpvgcoet.in/";

async function checkBackendStatus() {
  try {
    const start = Date.now();
    const res = await axios.get(URL, { timeout: 100000 });
    const end = Date.now();

    console.log("✅ Backend responded:", res.data || "OK");
    console.log(`⏱️ Response time: ${(end - start) / 1000}s`);
  } catch (err) {
    console.error("❌ Backend unreachable:", err.message);
    process.exit(1);
  }
}

const startTime = Date.now();
const duration = 5.5 * 3600 * 1000;

while (Date.now() - startTime < duration) {
  await checkBackendStatus();
  const istNow = new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' });
  console.log("☝️ Ping at", istNow);
  console.log("--------------------------");
  await new Promise(resolve => setTimeout(resolve, 5 * 60 * 1000));
}
