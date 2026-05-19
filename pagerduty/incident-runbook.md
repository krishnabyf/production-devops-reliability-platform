# Incident Management Runbook

## Severity Levels

### SEV1
Production outage, customers affected.

### SEV2
Major degradation, partial impact.

### SEV3
Minor issue, workaround available.

## Incident Flow

1. Alert triggered from Grafana/Prometheus
2. PagerDuty notifies on-call engineer
3. Engineer acknowledges incident
4. Check Grafana dashboard
5. Check Kubernetes pod status
6. Check Sentry errors
7. Rollback deployment if needed
8. Update stakeholders
9. Document root cause
10. Create prevention action items

## Useful Commands

```bash
kubectl get pods
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl rollout status deployment/devops-reliability-app
kubectl rollout undo deployment/devops-reliability-app
